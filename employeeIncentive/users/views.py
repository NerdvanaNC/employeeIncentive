from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from . import forms

# Create your views here.
def login_view(request):
  if request.method == 'POST':
    form = forms.LoginForm(request.POST)
    if form.is_valid():
      user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
      if user is not None:
        login(request, user)
        return redirect('/')
  else:
    form = forms.LoginForm()

  return render(request, 'users/login.html', {'form': form})

def logout_view(request):
  logout(request)
  return redirect('/')