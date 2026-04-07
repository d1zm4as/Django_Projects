from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.shortcuts import redirect, render

from .forms import CreateUserForm, LoginForm

# Create your views here.


def home(request):
    # return HttpResponse('Hello, World!')
    return render(request, "webapp/index.html")


# register a user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('login')
    context = {"form": form}
    return render(request, "webapp/register.html", context=context)


# login a user
def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("home")
    context = {"form": form}
    return render(request, "webapp/login.html", context=context)
