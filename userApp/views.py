from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import Register




class UserRegister(generic.CreateView):
    form_class = Register
    template_name =  'registration/register.html'
    success_url = reverse_lazy('login')


   

