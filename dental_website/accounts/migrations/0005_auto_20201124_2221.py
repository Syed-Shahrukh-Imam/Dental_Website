# Generated by Django 2.2.5 on 2020-11-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201124_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='info',
            field=models.TextField(default='I am a staff member', help_text='Personal Info', max_length=100),
        ),
    ]