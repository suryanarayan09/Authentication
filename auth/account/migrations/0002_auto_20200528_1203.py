# Generated by Django 3.0.4 on 2020-05-28 06:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='phone number must be entered in the form +919999999. Up to 10 digit', regex='^\\+?1?\\d{9,14}$')]),
        ),
    ]
