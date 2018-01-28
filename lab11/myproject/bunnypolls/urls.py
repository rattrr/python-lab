from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_form, name = 'index'),
    path('form_response/', views.form_response, name = 'form_response')
]
