from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm, LoginForm

# Create your views here.


def home(request):
    context = {}
    return render(request, "main/home.html", context)


def chores(request):
    context = {}
    return render(request, "main/chores.html", context)


def meals(request):
    context = {}
    return render(request, "main/meals.html", context)


def habits(request):
    context = {}
    return render(request, "main/habits.html", context)


def relax(request):
    context = {}
    return render(request, "main/relax.html", context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account created for {username}! You can now login."
            )
            return redirect("login")

    context = {"form": form}
    return render(request, "main/register.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")

    context = {"form": form}
    return render(request, "main/login.html", context)


def logoutPage(request):
    logout(request)
    return redirect("home")
