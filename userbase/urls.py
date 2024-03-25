from django.urls import path
from django.contrib.auth import views as auth_views

from userbase.views import MemberRegisterView, MemberLoginView, MemberLogoutView

urlpatterns = [
    path('login/', MemberLoginView.as_view(), name='login'),
    path('logout/', MemberLogoutView.as_view(), name='logout'),
    path('register/', MemberRegisterView.as_view(), name='register'),
]
