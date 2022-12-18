from decimal import Decimal

from django.contrib.gis.db import models


class Engine(models.Model):
    description = models.TextField(
        blank=True,
    )
    fuels = models.ManyToManyField(
        'Fuel',
    )
    isp = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    name = models.CharField(
        max_length=32,
    )

    def __str__(self):
        return self.name

    def get_fuels(self):
        return " ".join([str(f) for f in self.fuels.all()])


class Fuel(models.Model):
    acronym = models.CharField(
        max_length=32,
        blank=True,
        verbose_name='Fuel',
    )
    description = models.TextField(
        blank=True,
    )
    name = models.CharField(
        max_length=512,
        blank=True,
    )

    def __str__(self):
        if not self.acronym.strip():
            return self.name

        return self.acronym


class Rocket(models.Model):
    dry_mass = models.DecimalField(
        max_digits=19,
        decimal_places=5,
        default=Decimal(0),
        verbose_name="Dry Mass (kg)",
    )
    image = models.ImageField(
        upload_to='img/rocket',
        blank=True,
    )
    name = models.CharField(
        max_length=512,
    )
    stages = models.ManyToManyField(
        'Stage',
    )
    wet_mass = models.DecimalField(
        max_digits=19,
        decimal_places=5,
        default=Decimal(0),
        verbose_name="Wet Mass (kg)",
    )

    def __str__(self):
        return self.name

    def get_stages(self):
        return " ".join([str(s) for s in self.stages.all()])



class Stage(models.Model):
    engines = models.ManyToManyField(
        'Engine',
    )
    name = models.CharField(
        max_length=512,
    )
    tanks = models.ManyToManyField(
        'Tank',
    )

    def __str__(self):
        return self.name



class Tank(models.Model):
    capacity = models.DecimalField(
        max_digits=19,
        decimal_places=5,
        default=Decimal(0),
        verbose_name="Capacity (kg)",
    )
    fuel = models.ForeignKey(
        'Fuel',
        models.CASCADE,
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=512,
        blank=True,
    )
    volume = models.DecimalField(
        max_digits=19,
        decimal_places=5,
        default=Decimal(0),
        verbose_name="Volume (m³)"
    )
    dry_mass = models.DecimalField(
        max_digits=19,
        decimal_places=5,
        default=Decimal(0),
        verbose_name="Dry Mass (kg)",
    )

    def __str__(self):
        if not self.name.strip():
            return f"{self.fuel} - {self.capacity:,.2f} kg"

        return self.name
