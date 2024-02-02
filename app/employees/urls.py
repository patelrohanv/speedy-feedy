from django.urls import path
from . import views
from employees import views as employee_views

urlpatterns = [
    path("", views.employee_list, name="employee_list"),
    path("<int:pk>/", views.employee_detail, name="employee_detail"),
]
