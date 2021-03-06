# Generated by Django 2.2 on 2021-01-06 12:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('name', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('dateOfVisit', models.DateField(null=True)),
                ('status', models.CharField(choices=[('Yet to Fill CPNF', 'Yet to fill CPNF'), ('CPNF received, unscheduled', 'CPNF received, unscheduled'), ('OT scheduled', 'OT scheduled'), ('Interview scheduled', 'Interview scheduled'), (' Results received', ' Results received')], default='Yet to Fill CPNF', max_length=100)),
                ('existing_status', models.CharField(choices=[('Alive', 'Alive'), ('Dead', 'Dead')], default='Alive', max_length=100)),
                ('branchesAllowed', models.CharField(blank=True, default='', max_length=2000, null=True)),
                ('other_fields_url', models.URLField(blank=True, default='', null=True)),
                ('CGPA', models.FloatField(default=7.0)),
                ('companyID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Details')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('type_of_announcement', models.CharField(choices=[('Broadcasting', 'Broadcast'), ('Eligible', 'Eligible_ones')], default='Broadcasting', max_length=20)),
                ('announcementid', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('user', models.IntegerField()),
                ('datePublished', models.DateField(default=django.utils.timezone.now)),
                ('text', models.TextField(max_length=500)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Details')),
            ],
        ),
    ]
