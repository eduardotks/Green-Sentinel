from django.forms import ModelForm
from app.models import Sensor, User
from app.models import Planta


class SensorForm(ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'description', 'model', 'potency', 'duration', 'serial', 'brand']


class PlantaForm(ModelForm):
    class Meta:
        model = Planta
        fields = ['nome_cientifico', 'familia', 'pais_origem', 'cor', 'floracao', 'tamanho_medio', 'solo',
                  'luminosidade_preferida', 'frequencia_irrigacao']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'user_name', 'email', 'password']
