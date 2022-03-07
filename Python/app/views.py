from random import randrange

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import SensorForm
from app.models import Sensor, Measurer
from app.forms import PlantaForm
from app.models import Planta


# Create your views here.
def home(request):
    return HttpResponse('Hello World')


def sensor(request):
    data = {'db': Sensor.objects.all}
    return render(request, 'sensor.html', data)


def create_sensor(request):
    data = {'createSensor': SensorForm}
    return render(request, 'createSensor.html', data)

def create(request):
    form = SensorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(sensor)


def view_sensor(request, pk):
    data = {'db': Sensor.objects.get(pk=pk)}
    return render(request, 'viewSensor.html', data)


def edit_sensor(request, pk):
    data = {}
    data['db'] = Sensor.objects.get(pk=pk)
    data['createSensor'] = SensorForm(instance=data['db'])
    return render(request, 'createSensor.html', data)


def update_sensor(request, pk):
    data = {}
    data['db'] = Sensor.objects.get(pk=pk)
    form = SensorForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect(sensor)


def delete_sensor(request, pk):
    db = Sensor.objects.get(pk=pk)
    db.delete()
    return redirect(sensor)


def home_planta(request):
    data = {}
    data['db'] = Planta.objects.all()
    return render(request, 'index.html', data)


def form_planta(request):
    data = {}
    data['form_planta'] = PlantaForm()
    return render(request, 'form.html', data)


def create_planta(request):
    form = PlantaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_planta')


def view_planta(request, pk):
    data = {}
    data['db'] = Planta.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit_planta(request, pk):
    data = {}
    data['db'] = Planta.objects.get(pk=pk)
    data['form_planta'] = PlantaForm(instance=data['db'])
    return render(request, 'form.html', data)


def update_planta(request, pk):
    data = {}
    data['db'] = Planta.objects.get(pk=pk)
    form = PlantaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home_planta')


def delete_planta(request, pk):
    db = Planta.objects.get(pk=pk)
    db.delete()
    return redirect('home_planta')


def register_user(request):
    return render(request, 'registerUser.html')


def create_user(request):
    data = {}
    if request.POST['password'] != request.POST['password-conf']:
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'registerUser.html', data)


# Formulário do painel de login
def login_panel(request):
    return render(request, 'login.html')


# Processa o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return render(request, 'home.html')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'login.html', data)


def logouts(request):
    logout(request)
    return render(request, 'login.html')


def measurer(request):
    data = {'db': Measurer.objects.all}
    return render(request, 'measurer.html', data)


def simulator_measurer(request):
    data = {'db': Measurer.objects.all()}
    for measurer in data['db']:
        measurer.humidity = randrange(5, 100)
        measurer.temperature = randrange(10, 50)
        measurer.luminosity = randrange(20, 100)
        measurer.save()
    return render(request, 'measurer.html', data)
