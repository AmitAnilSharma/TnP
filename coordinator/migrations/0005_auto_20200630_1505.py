# Generated by Django 3.0.7 on 2020-06-30 15:05

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('coordinator', '0004_remove_companies_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='rollNumber',
        ),
        migrations.RemoveField(
            model_name='companies',
            name='yearOfGraduation',
        ),
        migrations.AddField(
            model_name='companies',
            name='branchesAllowed',
            field=models.CharField(blank=True, default='', max_length=200, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
