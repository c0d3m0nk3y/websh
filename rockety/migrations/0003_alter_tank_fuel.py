# Generated by Django 4.1.4 on 2022-12-17 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rockety', '0002_alter_engine_name_tank_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='fuel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rockety.fuel'),
        ),
    ]
