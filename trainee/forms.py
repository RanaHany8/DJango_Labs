from django import forms
from .models import Trainee

class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition',
                'placeholder': 'Enter full name...'
            })
        }

   
    def clean_name(self):
        name = self.cleaned_data.get('name')
        
     
        if name.isdigit():
            raise forms.ValidationError("Name cannot be numeric.")
            
       
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
            
        return name