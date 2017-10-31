from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_pw = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_pw)
            login(request, user)
            return redirect('notebook:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
