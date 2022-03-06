from django.db import models


# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    model = models.CharField(max_length=20)
    potency = models.CharField(max_length=5)
    duration = models.IntegerField()
    serial = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)


class Planta(models.Model):
    nome_cientifico = models.CharField(max_length=100)
    familia = models.CharField(max_length=100)
    pais_origem = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    floracao = models.CharField(max_length=100)
    tamanho_medio = models.DecimalField(max_digits=9, decimal_places=2)
    solo = models.CharField(max_length=100)
    luminosidade_preferida = models.CharField(max_length=100)
    frequencia_irrigacao = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Measurer(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.PROTECT)
    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT)
    luminosity = models.CharField(max_length=20)
    temperature = models.IntegerField()
    humidity = models.IntegerField()


def list_plantas(request):
    plantas = Planta.objects.all()
    return render(request, "plantas.html", {"plantas": plantas})


def create_planta(request):
    if form.is_valid():
        form.save()
        return redirect('list_plantas')
