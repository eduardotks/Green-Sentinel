from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import SensorForm
from app.models import Sensor
from app.forms import PlantaForm
from app.models import Planta
from app.models import ClientForm
from app.forms import ClientForm


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


def update_sensor(request, pk):
    data = {}
    data['db'] = Sensor.objects.get(pk=pk)
    data['createSensor'] = SensorForm(instance=data['db'])
    return render(request, 'createSensor.html', data)


def update(request, pk):
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


def create_client(request):
    form = ClientForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        return render(request, 'client.html')


def home_client(request):
    return render(request, 'client.html')


def form_client(request):
    data = {}
    data['form_client'] = ClientForm()
    return render(request, 'formClient.html', data)


def create_client(request):
    form_client = ClientForm(request.POST)
    if form_client.is_valid():
        form_client.save()
        return redirect('home_client')
    else:
        return render(request, 'client.html')
