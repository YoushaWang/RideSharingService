# Generated by Django 4.1.5 on 2023-02-07 20:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0020_remove_driver_user_delete_account_delete_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='multiSharer',
            field=models.ManyToManyField(blank=True, related_name='multiSharer', to=settings.AUTH_USER_MODEL),
        ),
    ]