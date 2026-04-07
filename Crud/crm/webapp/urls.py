from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("register.html", RedirectView.as_view(pattern_name="register", permanent=False)),
    path("login.html", RedirectView.as_view(pattern_name="login", permanent=False)),
]
