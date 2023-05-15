from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('parents', views.parents, name='parents'),
    path('students', views.students, name='students')
]