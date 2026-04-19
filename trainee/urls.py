from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.trainee_list),
    path('add/', views.add_trainee),
    path('update/<int:id>/', views.trainee_update),
    path('delete/<int:id>/', views.trainee_delete),
    path('<int:id>/', views.trainee_details),
]