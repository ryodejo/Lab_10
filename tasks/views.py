from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms_regis import RegisterForm



def home(request):
    return HttpResponse("Добро пожаловать в Django!")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})