from django.urls import path
from . import views

urlpatterns = [
    path('quizes/<str:slug>', views.quizes, name='quizes_page'),

    path('get_quizes/<str:slug>', views.get_quizes, name='get_quizes_page'),

    path('use_quiz/<str:slug>', views.use_quiz, name='use_quiz_page'),
    path('delete_quiz/<str:slug>', views.delete_quiz, name='delete_quiz_page'),
    path('test_quiz', views.test_quiz),

    path('set_quiz/<str:slug>', views.set_quiz, name='set_quiz_page'),
    path('save_quiz', views.save_quiz),

    path('assess_quiz/<str:slug>', views.assess_quiz, name='assess_quiz_page'),
]
