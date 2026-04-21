from django.urls import path
from . import views  

urlpatterns = [

    path('list/', views.TraineeListView.as_view(), name='trainee-list'),
    path('add/', views.TraineeCreateView.as_view(), name='trainee-add'),
    path('update/<int:pk>/', views.TraineeUpdateView.as_view(), name='trainee-update'), 
    path('delete/<int:pk>/', views.TraineeDeleteView.as_view(), name='trainee-delete'),
    path('<int:id>/', views.trainee_details, name='trainee-detail'),

    path('api/list/', views.trainee_list_create_api, name='api-trainee-list'),
    path('api/<int:id>/', views.trainee_detail_api, name='api-trainee-detail'),
]