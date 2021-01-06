# Generated by Django 2.2 on 2021-01-06 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='administrator', to=settings.AUTH_USER_MODEL),
        ),
    ]
