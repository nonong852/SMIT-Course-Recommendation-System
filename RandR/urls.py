from django.urls import path
from . import views

urlpatterns = [
    path('', views.RandR, name='RandR'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('look_up/', views.look_up, name='look_up'),
    
]
