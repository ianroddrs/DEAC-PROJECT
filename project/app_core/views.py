from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
    template = 'home.html'
    return render(request, template)

@login_required
def sair(request):
    template = 'login.html'
    logout(request)
    return render(request, template)

## test ##
@login_required
def testing(request):
  template = 'template.html'
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return render(request, template, context)