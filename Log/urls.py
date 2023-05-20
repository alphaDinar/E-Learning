from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('logout', views.logout_page, name='logout_page'),
    path('portal', views.portal, name='portal'),
    # path('student_portal', views.student_portal, name='student_portal'),
    path('teacher_portal', views.teacher_portal, name='teacher_portal'),
]
