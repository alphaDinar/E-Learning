from django.urls import path
from . import views

urlpatterns = [
    path('student_dashboard', views.student_dash, name='student_dash'),
    
    path('student_quizes', views.student_quizes, name='student_quizes_page'),
    
    path('student_get_quizes_schemes/<str:slug>', views.student_get_quizes_schemes, name='student_get_quizes_schemes_page'),
    
    path('student_get_quizes/<str:slug>', views.student_get_quizes, name='student_get_quizes_page'),
    
    path('student_start_quiz/<str:slug>', views.student_start_quiz, name='student_start_quiz_page'),
    path('mark_quiz', views.mark_quiz),

    path('student_quiz_results/<int:id>', views.student_quiz_results, name='student_quiz_results_page')
]
