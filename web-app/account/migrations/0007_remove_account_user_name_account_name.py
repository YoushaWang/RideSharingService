# Generated by Django 4.1.5 on 2023-01-30 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0006_alter_account_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user_name',
        ),
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
