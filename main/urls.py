from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("meals/", views.meals, name="meals"),
    path("chores/", views.chores, name="chores"),
    path("habits/", views.habits, name="habits"),
    path("relax/", views.relax, name="relax"),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutPage, name="logout"),
]
