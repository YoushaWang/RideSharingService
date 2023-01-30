# Generated by Django 4.1.5 on 2023-01-30 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0016_alter_userdetail_car_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='car_type',
            field=models.CharField(choices=[('NONE', 'NONE'), ('SUV', 'SUV'), ('COMPACT', 'COMPACT'), ('COMFORT', 'COMFORT'), ('GREEN', 'GREEN'), ('PREMIER', 'PREMIER')], default='SUV', max_length=20),
        ),
        migrations.AddField(
            model_name='ride',
            name='driver',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='ride',
            name='extraInfo',
            field=models.CharField(default='NONE', max_length=200),
        ),
        migrations.AddField(
            model_name='ride',
            name='ifShare',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ride',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ride',
            name='pickup',
            field=models.CharField(default='NONE', max_length=100),
        ),
        migrations.AddField(
            model_name='ride',
            name='schedule',
            field=models.DateTimeField(default='2023-02-01'),
        ),
        migrations.AddField(
            model_name='ride',
            name='sharer',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='ride',
            name='sharer_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('COMFIRM', 'COMFIRM'), ('COMPLETE', 'COMPLETE')], default='OPEN', max_length=20),
        ),
        migrations.AddField(
            model_name='ride',
            name='whereto',
            field=models.CharField(default='NONE', max_length=100),
        ),
    ]
