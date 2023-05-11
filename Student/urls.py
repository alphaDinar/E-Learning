from django.urls import path
from . import views

urlpatterns = [
    path('student_dashboard', views.student_dash, name='student_dash'),
]
