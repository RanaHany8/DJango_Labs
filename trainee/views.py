from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee


def trainee_list(request):
    all_trainees = Trainee.objects.all()
    return render(request, 'trainee/list.html', {'trainees': all_trainees})

def add_trainee(request):
    errors = {}
    if request.method == 'POST':
        t_name = request.POST.get('trainee_name', '').strip()
        
  
        if len(t_name) < 3:
            errors['name'] = "Name must be at least 3 characters long."
        
  
        elif any(char.isdigit() for char in t_name):
            errors['name'] = "Name must contain letters only. Numbers are not allowed."
            
  
        if not errors:
            Trainee.objects.create(name=t_name)
            return redirect('/trainee/list/')

    return render(request, 'trainee/add.html', {'errors': errors})


def trainee_details(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    return render(request, 'trainee/traineedetaile.html', {'trainee': trainee})


def trainee_delete(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete()
    return redirect('/trainee/list/') 


def trainee_update(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    errors = {}
    if request.method == 'POST':
        new_name = request.POST.get('trainee_name', '').strip()
        
    
        if len(new_name) < 3:
            errors['name'] = "Name is too short."

        elif any(char.isdigit() for char in new_name):
            errors['name'] = "Numbers are not allowed in the name."
            
        if not errors:
            trainee.name = new_name
            trainee.save()
            return redirect('/trainee/list/') 
            
    return render(request, 'trainee/update.html', {'trainee': trainee, 'errors': errors})