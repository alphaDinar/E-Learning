from django.urls import path
from . import views

urlpatterns = [
    path('student_dashboard', views.student_dash, name='student_dash'),
    path('student_sideBar', views.student_sideBar),

    path('student_slides', views.student_slides, name='student_slides_page'),
    path('student_get_slides_schemes/<str:slug>', views.student_get_slides_schemes, name='student_get_slides_schemes_page'),
    path('student_get_slide/<str:slug>', views.student_get_slide  , name='student_get_slide_page'),
    path('toggle_res_status', views.toggle_res_status),
    path('rate_scheme', views.rate_scheme),

    path('student_quizes', views.student_quizes, name='student_quizes_page'),
    path('student_get_quizes_schemes/<str:slug>', views.student_get_quizes_schemes, name='student_get_quizes_schemes_page'),
    path('student_get_quizes/<str:slug>', views.student_get_quizes, name='student_get_quizes_page'),
    path('student_start_quiz/<str:slug>', views.student_start_quiz, name='student_start_quiz_page'),
    path('mark_quiz', views.mark_quiz),
    path('student_quiz_results/<int:id>', views.student_quiz_results, name='student_quiz_results_page'),
    path('student_quiz_history/<str:slug>', views.student_quiz_history, name='student_quiz_history_page'),

    path('student_assignments', views.student_assignments, name='student_assignments_page'),
    path('student_get_assignments_schemes/<str:slug>', views.student_get_assignments_schemes, name='student_get_assignments_schemes_page'),
    path('student_get_assignments/<str:slug>', views.student_get_assignments, name='student_get_assignments_page'),
    path('student_start_assignment/<str:slug>', views.student_start_assignment, name='student_start_assignment_page'),
    path('mark_assignment', views.mark_assignment),
    path('student_assignment_results/<int:id>', views.student_assignment_results, name='student_assignment_results_page'),
    path('student_assignment_history/<str:slug>', views.student_assignment_history, name='student_assignment_history_page'),

    path('student_liveclasses', views.student_liveclasses, name='student_liveclasses_page' ),
    
    path('student_assessment', views.student_assessment, name='student_assessment_page'),
    path('student_assessment_quizes/<str:slug>', views.student_assessment_quizes, name='student_assessment_quizes_page'),

    path('student_events', views.student_events , name='student_events_page'),
    path('student_noticeboard', views.student_noticeboard, name='student_noticeboard_page'),

    path('student_report', views.student_report, name='student_report_page'),

    path('mark2', views.mark2)
]
