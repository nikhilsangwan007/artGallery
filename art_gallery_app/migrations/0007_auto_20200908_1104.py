# Generated by Django 3.1 on 2020-09-08 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_gallery_app', '0006_auto_20200908_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='year_of_publish',
            field=models.DateField(),
        ),
    ]