# Generated by Django 2.2.5 on 2020-11-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20201124_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='notes',
            field=models.TextField(help_text='Booking Notes', max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
