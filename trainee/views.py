from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Trainee
from .forms import TraineeForm


class TraineeListView(ListView):
    model = Trainee
    template_name = 'trainee/list.html'
    context_object_name = 'trainees'


def trainee_details(request, id):
    from django.shortcuts import render, get_object_or_404
    trainee = get_object_or_404(Trainee, id=id)
    return render(request, 'trainee/traineedetaile.html', {'trainee': trainee})


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