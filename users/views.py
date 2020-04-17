from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request, user)
            return redirect('order_list')
        else:
            messages.error(request, "El usuario o contraseña son invalidos")
            return render(request,'users/sign_in.html')
    return render(request,'users/sign_in.html')

@login_required
def log_out(request):
    logout(request)
    return redirect('sign_in')