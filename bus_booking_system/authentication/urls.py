from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('passenger/dashboard.html/', views.passenger_dashboard, name='passenger_dashboard'),
    path('admin/dashboard.html', views.admin_dashboard, name="admin_dashboard"),
    path('register/', views.register, name='register'),

    path('', include('django.contrib.auth.urls')),
]