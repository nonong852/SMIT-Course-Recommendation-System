"""
URL configuration for nproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from RandR import views as RandR_views  # Import RandR views with alias
from Recommender import views as Recommender_views  # Import Recommender views with alias
from home import views as home_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Recommender/', include(('Recommender.urls', 'Recommender'), namespace='Recommender')),
    path('RandR/', include(('RandR.urls', 'RandR'), namespace='RandR')),
    path('About/', include(('About.urls', 'About'), namespace='About')),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('submit_review/', RandR_views.submit_review, name='submit_review'),  # Use RandR_views for RandR views
    path('look_up/', RandR_views.look_up, name='look_up'),  # Use RandR_views for RandR views
    path('coursedetails/<int:course_id>/', Recommender_views.coursedetails, name='coursedetails'),# Use Recommender_views for Recommender views
    path('filter_courses/', Recommender_views.filter_courses, name='filter_courses'),
    path('course/<int:course_id>/', home_views.coursedetails, name='course_detail'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
