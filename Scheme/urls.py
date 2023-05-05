from django.urls import path
from . import views

urlpatterns = [
    path('schemes/<str:slug>', views.schemes, name='schemes_page'),
    path('use_scheme/<str:slug>', views.use_scheme, name='use_scheme_page'),
    path('edit_scheme/<str:slug>', views.edit_scheme, name='edit_scheme_page'),

    path('edit_scheme/<str:slug>/delete_image/<int:id>', views.delete_image, name='delete_image')
]
