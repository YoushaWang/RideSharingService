# Generated by Django 4.1.5 on 2023-01-30 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_userdetail_car_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='car_type',
            field=models.CharField(blank=True, choices=[('NONE', 'NONE'), ('SUV', 'SUV'), ('COMPACT', 'COMPACT'), ('COMFORT', 'COMFORT'), ('GREEN', 'GREEN'), ('PREMIER', 'PREMIER')], default='NONE', max_length=20, null=True),
        ),
    ]
