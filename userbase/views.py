from django.shortcuts import render
from django.views.generic import TemplateView


class MemberRegisterView(TemplateView):
    template_name = 'register.html'
