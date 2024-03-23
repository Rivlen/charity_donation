from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from userbase.forms import UserForm
from userbase.models import CustomUser


class MemberRegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        new_user = UserForm(request.POST)
        new_user.save()
        return redirect(reverse('login'))


class MemberLoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username="john", password="secret")
        if user is not None:
            login(request, user)
            return redirect(reverse('landing-page'))
        else:
            return redirect(reverse('register'))
