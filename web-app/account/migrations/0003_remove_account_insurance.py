# Generated by Django 4.1.5 on 2023-01-29 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_account_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='insurance',
        ),
    ]
