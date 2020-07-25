# Generated by Django 3.0.8 on 2020-07-21 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=200)),
                ('apellido', models.TextField(max_length=200)),
                ('domicilio', models.TextField(max_length=500)),
                ('dni', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('genero', models.TextField()),
                ('fecha_nac', models.IntegerField()),
            ],
        ),
    ]