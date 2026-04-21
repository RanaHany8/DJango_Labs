from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Trainee
from .forms import TraineeForm
from .serializers import TraineeSerializer

# --- Template Views (HTML) ---
class TraineeListView(ListView):
    model = Trainee
    template_name = 'trainee/list.html'
    context_object_name = 'trainees'

class TraineeCreateView(CreateView):
    model = Trainee
    form_class = TraineeForm
    template_name = 'trainee/add.html'
    success_url = reverse_lazy('trainee-list')

class TraineeUpdateView(UpdateView):
    model = Trainee
    form_class = TraineeForm
    template_name = 'trainee/update.html'
    success_url = reverse_lazy('trainee-list')

class TraineeDeleteView(DeleteView):
    model = Trainee
    template_name = 'trainee/delete.html'
    success_url = reverse_lazy('trainee-list')

def trainee_details(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    return render(request, 'trainee/traineedetaile.html', {'trainee': trainee})

# --- API Views (JSON) ---
@api_view(['GET', 'POST'])
def trainee_list_create_api(request):
    if request.method == 'GET':
        trainees = Trainee.objects.all()
        serializer = TraineeSerializer(trainees, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TraineeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def trainee_detail_api(request, id):
    try:
        trainee = Trainee.objects.get(id=id)
    except Trainee.DoesNotExist:
        return Response({'error': 'Trainee not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TraineeSerializer(trainee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TraineeSerializer(trainee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        trainee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)