from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # this actually saves the inputted info and creates user -> also hashes password
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('golf-round-home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
