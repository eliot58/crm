import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .tasks import saveworks
from django.contrib.auth.decorators import login_required
from .models import Client, Log, File, Calculator, Work
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.conf import settings
from datetime import datetime, timedelta
import requests
import json



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
    if request.user.is_superuser:
        logout(request)
        return redirect(login_view)
    
    works = Work.objects.filter(manager_id = request.user.manager.id).order_by("-last_order_date")

    if request.user.manager.last_works_update:
        if request.user.manager.last_works_update - datetime.now().date() > timedelta(days = 1):
            r = requests.get(f"http://176.62.187.250/agent.php")

            try:
                agents = json.loads(r.text)
            except json.decoder.JSONDecodeError:
                r = requests.get(f"http://176.62.187.250/agent.php")
                agents = json.loads(r.text)

            filtered = list(filter(lambda item: True if request.user.username.lower().find(item["manager"].lower()) != -1 else False, agents))

            agents = sorted(filtered, key = lambda item: item["last_order_date"], reverse = True)

            saveworks.delay(agents, request.user.manager.id)

            manager = request.user.manager

            manager.last_works_update = datetime.now().date()

            manager.save()

        else:
            agents = works

    else:  
        r = requests.get(f"http://176.62.187.250/agent.php")

        try:
            agents = json.loads(r.text)
        except json.decoder.JSONDecodeError:
            r = requests.get(f"http://176.62.187.250/agent.php")
            agents = json.loads(r.text)

        filtered = list(filter(lambda item: True if request.user.username.lower().find(item["manager"].lower()) != -1 else False, agents))

        agents = sorted(filtered, key = lambda item: item["last_order_date"], reverse = True)

        saveworks.delay(agents, request.user.manager.id)

        manager = request.user.manager

        manager.last_works_update = datetime.now().date()

        manager.save()
    
    return render(request, 'index.html', {"clients": Client.objects.all(), "calcs": Calculator.objects.all(), "agents": agents})


@require_POST
def createClient(request):
    if not request.user.manager:
        return HttpResponseForbidden()
    client = Client()
    try:
        client.name_point = request.POST["name_point"]
    except KeyError:
        pass

    try:
        client.fullName = request.POST["fullName"]
    except KeyError:
        pass

    try:
        client.address = request.POST["address"]
    except KeyError:
        pass

    try:
        client.region = request.POST["region"]
    except KeyError:
        pass

    try:
        client.director_phone = request.POST["director_phone"]
    except KeyError:
        pass

    try:
        client.manager_phone = request.POST["manager_phone"]
    except KeyError:
        pass


    try:
        client.email = request.POST["email"]
    except KeyError:
        pass

    try:
        client.with_work = request.POST["with_work"]
    except KeyError:
        pass

    try:
        client.photo = request.FILES["photo"]
    except KeyError:
        pass
    client.save()

    log = Log()
    log.manager = request.user.manager
    log.client = client
    log.comment = "Создание клиента"
    log.save()

    return redirect(index)

def get_logs(_, id):
    logs = Log.objects.filter(client_id = id)
    res = []
    for log in logs:
        res.append(log.__str__())
    return JsonResponse({"logs": res})

@require_POST
def updateClient(request, id):
    client = Client.objects.get(id = id)
    if request.POST["name_point"] != client.name_point:
        log = Log()
        log.manager = request.user.manager
        log.client = client
        log.comment = f"Изменено название торговой точки с {client.name_point} на {request.POST['name_point']}"
        log.save()
        client.name_point = request.POST["name_point"]

    if request.POST["fullName"] != client.fullName:
        log = Log()
        log.manager = request.user.manager
        log.client = client
        log.comment = f"Изменено ФИО с {client.fullName} на {request.POST['fullName']}"
        log.save()
        client.fullName = request.POST["fullName"]

    if request.POST["address"] != client.address:
        log = Log()
        log.manager = request.user.manager
        log.client = client
        log.comment = f"Изменен адрес с {client.address} на {request.POST['address']}"
        log.save()
        client.address = request.POST["address"]

    if request.POST["region"] != client.region:
        log = Log()
        log.manager = request.user.manager
        log.client = client
        log.comment = f"Изменен регион с {client.region} на {request.POST['region']}"
        log.save()
        client.region = request.POST["region"]

    if request.POST["director_phone"] != client.director_phone:
        log = Log()
        log.manager = request.user.manager
        log.client = client
        log.comment = f"Изменен номер телефона собственника с {client.director_phone} на {request.POST['director_phone']}"
        log.save()
        client.director_phone = request.POST["director_phone"]


    if request.POST["manager_phone"] != client.manager_phone:
        log = Log()
        log.manager = request.user.manager
        log.client = client
        log.comment = f"Изменен номер телефона менеджера с {client.manager_phone} на {request.POST['manager_phone']}"
        log.save()
        client.manager_phone = request.POST["manager_phone"]

    if request.POST["email"] != client.email:
        log = Log()
        log.manager = request.user.manager
        log.client = client
        log.comment = f"Изменен email с {client.email} на {request.POST['email']}"
        log.save()
        client.email = request.POST["email"]

    if request.POST["with_work"] != client.with_work:
        log = Log()
        log.manager = request.user.manager
        log.client = client
        log.comment = f"Изменено поле с кем работает с {client.with_work} на {request.POST['with_work']}"
        log.save()
        client.with_work = request.POST["with_work"]


    try:
        client.photo = request.FILES['photo']
    except KeyError:
        pass
    client.save()

    if "comment" in request.POST:
        log = Log()
        log.manager = request.user.manager
        log.client = client
        log.comment = f"Комментарий: {request.POST['comment']}"
        log.save()

    return redirect(index)

@csrf_exempt
def take(request, id):
    client = Client.objects.get(id = id)
    if request.POST["is_take"] == "1":
        client.potential = request.user.manager
        client.save()
        log = Log()
        log.manager = request.user.manager
        log.client = client
        log.comment = f"Взят в работу комментарий {request.POST['comment']}"
        log.save()
    else:
        log = Log()
        log.manager = request.user.manager
        log.client = client
        log.comment = f"Не взят в работу комментарий {request.POST['comment']}"
        log.save()
    return redirect(index)

@csrf_exempt
def refuse(request, id):
    client = Client.objects.get(id = id)
    client.potential = None
    client.save()
    log = Log()
    log.manager = request.user.manager
    log.client = client
    log.comment = f"Отказ комментарий {request.POST['comment']}"
    log.save()
    return redirect(index)

@csrf_exempt
def no_target(request, id):
    client = Client.objects.get(id = id)
    client.potential = None
    client.save()
    log = Log()
    log.manager = request.user.manager
    log.client = client
    log.comment = f"Отказ комментарий {request.POST['comment']}"
    log.save()
    return redirect(index)

def send_calc(request, id):
    file = File()
    file.file = request.FILES["file"]
    file.save()
    client = Client.objects.get(id = id)
    log = Log()
    log.manager = request.user.manager
    log.client = client
    log.comment = f"Отправлено расчетчику комментарий: {request.POST['comment']}"
    log.file = file
    log.save()
    email = EmailMessage(f"Потенциальный клиент от пользователя {request.user.username}", request.POST["comment"], settings.EMAIL_HOST_USER, [Calculator.objects.get(id = int(request.POST['calc'])).email])
    if settings.DEBUG:
        print(settings.MEDIA_ROOT + '/' + file.file.url[7::])
        with open(settings.MEDIA_ROOT + '/' + file.file.url[7::], 'rb') as f:
            email.attach(os.path.basename(settings.MEDIA_ROOT + '/' + file.file.url[7::]), f.read(), 'text/plain')
        
    email.send()
    return redirect(index)

def createDiler(request):
    query = f"exec pg_create_customer_for_lk '{request.user.manager.idpeople}', '{request.POST['fullName']}', '{request.POST['address']}', '{request.POST['director_phone']}', '{request.POST['manager_phone']}', '{request.POST['email']}', '{request.POST['login']}', '{request.POST['password']}'"

    requests.post(f'http://176.62.187.250/createService.php', data={"query": query})
    return redirect(index)


@csrf_exempt
def validate(request):
    try:
        Client.objects.get(director_phone = request.POST["director_phone"])
        return JsonResponse({"director_phone": False})
    except Client.DoesNotExist:
        work = Work.objects.filter(phone = request.POST["director_phone"])
        if len(work) == 0:
            return JsonResponse({"director_phone": True})
        return JsonResponse({"director_phone": False})