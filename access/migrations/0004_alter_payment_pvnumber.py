# Generated by Django 4.1.7 on 2023-06-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0003_payment_pvnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='PVNumber',
            field=models.IntegerField(default=0),
        ),
    ]
