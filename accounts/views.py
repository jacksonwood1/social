from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import (FormView, CreateView,
                                        UpdateView, DeleteView)

from accounts import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
