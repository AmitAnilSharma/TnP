# Generated by Django 3.0.7 on 2020-07-01 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_auto_20200630_1519'),
        ('coordinator', '0011_auto_20200701_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='branchesAllowed',
        ),
        migrations.AddField(
            model_name='companies',
            name='branchesAllowed',
            field=models.ManyToManyField(to='administrator.Branch'),
        ),
    ]
