# Generated by Django 4.0.4 on 2022-05-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodegas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=30)),
                ('departamento', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('tipoUsuario', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vinos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varietal', models.CharField(max_length=30)),
                ('bodega', models.CharField(max_length=30)),
                ('año', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
