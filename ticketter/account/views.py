from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserRegisterForm


def home(request):
    return render(request=request, template_name='account/home.html', context={})


def about(request):
    return render(request=request, template_name='account/about.html', context={})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request=request, message=f"{username} may now login!")
            return redirect(to='account-login')
    else:
        form = UserRegisterForm()
    return render(request=request, template_name='account/register.html', context={'form': form})