# Generated by Django 4.1.3 on 2022-12-17 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerapp', '0004_alter_equipo_apodo_alter_equipo_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='titInternac',
            field=models.IntegerField(default=0),
        ),
    ]
