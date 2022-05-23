from django.urls import path
from django.contrib.auth import views as auth_view
from .views import Home, Signup


urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('signup', Signup.as_view(), name='signup'),
  path('login', auth_view.LoginView.as_view(), name='login'),
  path('logout', auth_view.LogoutView.as_view(), name='logout'),
]