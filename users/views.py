from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from django.contrib.auth import logout
from .forms import SignupForm
# Create your views here.

class UserLogin(LoginView):
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse_lazy("home")


class UserLogout(View):

    def get(self, request):
        logout(request)
        return redirect("login")

class UserSignup(CreateView):
    template_name = "users/signup.html"
    success_url = reverse_lazy("login")
    form_class = SignupForm

    def form_valid(self,form):
        #If the data is valid, record will be saved 
        user = form.save(commit=False)
        pass_text = form.cleaned_data["password"]
        user.set_password(pass_text) #encrypt/has the password
        user.save()

        return super().form_valid(form)
