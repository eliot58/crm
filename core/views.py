from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.decorators.http import require_POST


#LOGIN LOGOUT
#============================================================================
def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
            if user.is_active:
                login(request, user)
                return redirect(index)
    else:
        if request.user.is_authenticated:
            return redirect(index)
        login_form = LoginForm()
    return render(request, 'login.html', {'form': login_form})


def logout_view(request):
    logout(request)
    return redirect(login_view)



@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html', {"commonbase": Client.objects.all()})


@require_POST
def commonBase(request):
    client = Client()
    client.name_point = request.POST["name_point"]
    client.fullName = request.POST["fullName"]
    client.address = request.POST["address"]
    client.region = request.POST["region"]
    client.director_phone = request.POST["director_phone"]
    client.manager_phone = request.POST["manager_phone"]
    client.email = request.POST["email"]
    client.with_work = request.POST["with_work"]
    try:
        client.photo = request.FILES['photo']
    except KeyError:
        pass
    client.comment = request.POST["comment"]
    client.save()
    return redirect(index)
