# Generated by Django 2.2.5 on 2020-11-24 07:31

import accounts.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201124_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='insurance_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10), accounts.models.insurance_validator]),
        ),
    ]
