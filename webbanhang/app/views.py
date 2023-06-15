from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    return render(request, 'app/home.html')


def introduction(request):
    return render(request, 'app/introduction.html')


def contact(request):
    return render(request, 'app/contact.html')


def cart(request):
    return render(request, 'app/cart.html')


def error(request, exception):
    message = {
        'message': exception
    }
    return render(request, 'app/404.html', message)


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'app/register.html', {'form': form})
