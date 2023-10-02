from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.create_employee, name='create_employee'),
    path('employee/<int:regid>/', views.update_employee, name='update_employee'),
    path('employee/delete/', views.delete_employee, name='delete_employee'),
    path('employee/get/', views.get_employee, name='get_employee'),
]
