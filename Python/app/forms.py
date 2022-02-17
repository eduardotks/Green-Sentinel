from django.forms import ModelForm
from app.models import Sensor


class SensorForm(ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'description', 'model', 'potency', 'duration', 'serial', 'brand']
