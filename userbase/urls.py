from django.urls import path
from django.contrib.auth import views as auth_views

from userbase.views import UserRegisterView, UserLoginView, UserLogoutView, UserDetailsView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('details/', UserDetailsView.as_view(), name='user-details'),
]
