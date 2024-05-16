from django.urls import path
from . import views

urlpatterns = [
    path('', views.Recommender, name='Recommender'),
    path('coursedetails/<int:course_id>/', views.coursedetails, name='coursedetails'),
    path('filter_courses/', views.filter_courses, name='filter_courses'),
]
