# Generated by Django 3.0.7 on 2020-06-30 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinator', '0005_auto_20200630_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='CTC',
            field=models.FloatField(),
        ),
    ]
