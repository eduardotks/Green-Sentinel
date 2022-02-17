from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import SensorForm
from app.models import Sensor


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
