from django.urls import path
from . import views

urlpatterns = [
    path('supermanager', views.supermanager, name='supermanager_page'),
    
    path('super_student_assessment', views.super_student_assessment, name='super_student_assessment_page'),
    path('super_get_student_assessment/<str:slug>', views.super_get_student_assessment, name='super_get_student_assessment_page'),

    path('super_add_student', views.super_add_student, name='super_add_student_page'),
    path('super_get_students/<str:slug>', views.super_get_students, name='super_get_students_page'),
    path('super_delete_student', views.super_delete_student),

    path('super_add_teacher', views.super_add_teacher, name='super_add_teacher_page'),
    # path('super_get_teachers/<str:slug>', views.super_get_teachers, name='super_get_teachers_page'),
    # path('super_delete_teacher', views.super_delete_teacher),

    path('super_grades/', views.super_grades, name='super_grades_page'),
    path('super_delete_grade', views.super_delete_grade),

    path('super_get_grade/<str:slug>', views.super_get_grade, name='super_get_grade_page'),
    path('super_delete_course', views.super_delete_course),

    path('super_test', views.super_test, name='super_test_page'),

]