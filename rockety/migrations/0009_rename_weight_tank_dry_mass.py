# Generated by Django 4.1.4 on 2022-12-18 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rockety', '0008_rocket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tank',
            old_name='weight',
            new_name='dry_mass',
        ),
    ]
