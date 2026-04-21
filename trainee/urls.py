
from django.urls import path
from .views import *

urlpatterns = [
    path('list/', TraineeListView.as_view(), name='trainee-list'),
    path('add/', TraineeCreateView.as_view(), name='trainee-add'),
    path('update/<int:pk>/', TraineeUpdateView.as_view(), name='trainee-update'), 
    path('delete/<int:pk>/', TraineeDeleteView.as_view(), name='trainee-delete'),
    path('<int:id>/', trainee_details, name='trainee-detail'),
]