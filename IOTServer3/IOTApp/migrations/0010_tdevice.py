# Generated by Django 2.0.5 on 2018-05-23 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('IOTApp', '0009_auto_20180517_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='tDevice',
            fields=[
                ('DeviceSeq', models.AutoField(primary_key=True, serialize=False, verbose_name='Device Sequence')),
                ('DeviceNo', models.CharField(max_length=20, null=True, verbose_name='Device No')),
                ('DeviceName', models.CharField(max_length=20, null=True, verbose_name='Device Name')),
                ('DeviceType', models.CharField(blank=True, choices=[('1', 'sensor'), ('2', 'controller'), ('3', 'gateway'), ('4', 'server')], max_length=1, null=True, verbose_name='Device Type')),
                ('Remark', models.CharField(blank=True, max_length=20, null=True, verbose_name='Remark')),
                ('RegDT', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Register DateTime')),
                ('UptDT', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Update DateTime')),
                ('RegUserSeq', models.ForeignKey(db_column='RegUserSeq', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Register')),
                ('UptUserSeq', models.ForeignKey(db_column='UptUserSeq', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Device',
            },
        ),
    ]
