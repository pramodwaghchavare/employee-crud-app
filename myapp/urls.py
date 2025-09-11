# from django.urls import path
# from .views import add_employee, delete_employee, hello_world, update_employee
# from .views import create_message
# from .views import employee_list


# urlpatterns = [
   
#     path('employees/', employee_list, name='employee_list'),
#     path('employees/add/', add_employee, name='add_employee'),
#     path('employees/<int:pk>/', update_employee, name='update-employee'),
#       path('employees/<int:pk>/delete/', delete_employee, name='delete-employee')
# ]

# employees/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/<int:pk>/update/', views.update_employee, name='update_employee'),
    path('employees/<int:pk>/delete/', views.delete_employee, name='delete_employee'),
]

