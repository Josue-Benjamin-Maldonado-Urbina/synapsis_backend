# Generated by Django 5.1.2 on 2024-12-11 05:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('cat', 'Gato'), ('dog', 'Perro'), ('bird', 'Ave'), ('fish', 'Pez'), ('aquatic', 'Animal Acuático'), ('other', 'Otro (Insecto/Reptil)')], max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pet_images/')),
                ('gender', models.CharField(choices=[('male', 'Macho'), ('female', 'Hembra')], max_length=10)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('breed', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('illness', models.CharField(max_length=100)),
                ('illness_gravity', models.CharField(choices=[('low', 'No Grave'), ('high', 'Grave')], max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='client.owner')),
            ],
        ),
    ]
