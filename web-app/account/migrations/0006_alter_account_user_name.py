# Generated by Django 4.1.5 on 2023-01-30 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_account_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
