# Generated by Django 3.1 on 2020-09-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_gallery_app', '0008_auto_20200908_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paintings',
            name='year_of_publish',
            field=models.DateField(),
        ),
    ]