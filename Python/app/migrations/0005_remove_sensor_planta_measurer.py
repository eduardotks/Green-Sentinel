# Generated by Django 4.0.2 on 2022-03-06 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_sensor_planta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='planta',
        ),
        migrations.CreateModel(
            name='Measurer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('luminosity', models.CharField(max_length=20)),
                ('temperature', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.planta')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sensor')),
            ],
        ),
    ]