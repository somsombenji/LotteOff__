# Generated by Django 3.1.2 on 2020-10-10 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driveApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drivethru',
            name='items',
        ),
        migrations.AlterField(
            model_name='drivethru',
            name='pick_date',
            field=models.CharField(max_length=20),
        ),
    ]
