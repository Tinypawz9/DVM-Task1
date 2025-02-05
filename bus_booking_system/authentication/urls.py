from django.urls import path
from .views import login_view, home
urlpatterns = [
    path('login/', login_view, name='login'),
    path('home/', home, name='home_page'),
]