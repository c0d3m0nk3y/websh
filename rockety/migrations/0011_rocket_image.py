# Generated by Django 4.1.4 on 2022-12-18 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rockety', '0010_alter_tank_dry_mass'),
    ]

    operations = [
        migrations.AddField(
            model_name='rocket',
            name='image',
            field=models.ImageField(blank=True, upload_to='img/rocket'),
        ),
    ]
