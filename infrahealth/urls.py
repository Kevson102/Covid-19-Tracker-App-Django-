from .views import RegisterAPI, LoginAPI
from knox import views as knox_views
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/healthcheck/', views.HealthCheck),
    url(r'^api/healthcheck/([0-9]+)$', views.HealthCheck),
    path('api/response/', views.Answers),
    url(r'^api/response/([0-9]+)$', views.Answers), 
]
