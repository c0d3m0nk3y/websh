# Generated by Django 4.1.4 on 2022-12-17 15:45

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rockety', '0004_tank_name_alter_tank_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='capacity',
            field=models.DecimalField(decimal_places=5, default=Decimal('0'), max_digits=19, verbose_name='Capacity (kg)'),
        ),
    ]