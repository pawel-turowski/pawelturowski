from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie pomyślne')
                else:
                    return HttpResponse('Konto zablokowane')
            else:
                return HttpResponse('Nieprawidłowe dane')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form' : form})

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home_page')
    template_name = 'account/signup.html'

class MyAccount(TemplateView):
    template_name = 'account/my_account.html'

