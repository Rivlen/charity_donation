from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from userbase.forms import UserForm


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        new_user = UserForm(request.POST)
        if new_user.is_valid():
            password = new_user.cleaned_data['password1']
            user = new_user.save(commit=False)
            user.set_password(password)
            user.save()

            return redirect(reverse('login'))
        return render(request, 'register.html')


class UserLoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('landing-page'))
        else:
            return redirect(reverse('register'))


class UserLogoutView(View):
    def get(self, request):
        request.session.clear()
        return redirect(reverse('landing-page'))


class UserDetailsView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        return render(request, 'user-details.html')
