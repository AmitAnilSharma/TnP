# Generated by Django 3.0.7 on 2020-07-01 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20200701_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='coordinators',
        ),
    ]
