from django.urls import path
from . import views

app_name='home'
urlpatterns = [
    path('', views.home, name='home'),
    path('transfer-courses/', views.transfer_courses, name='transfer_courses'),
    path('course/<int:course_id>/', views.coursedetails, name='course_detail'),
    ]