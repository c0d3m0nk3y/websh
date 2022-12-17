from decimal import Decimal

from django.contrib.gis.db import models


class Fuel(models.Model):
    name = models.CharField(
        max_length=512,
        blank=True,
    )
    acronym = models.CharField(
        max_length=32,
        blank=True,
    )
    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        if not self.acronym.strip():
            return self.name

        return self.acronym


class Engine(models.Model):
    name = models.CharField(
        max_length=32,
    )
    description = models.TextField(
        blank=True,
    )
    isp = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    fuels = models.ManyToManyField(
        'Fuel',
    )

    def __str__(self):
        return self.name

    def get_fuels(self):
        return "\n".join([str(f) for f in self.fuels.all()])


class Stage(models.Model):
    name = models.CharField(
        max_length=512,
    )
    tanks = models.ManyToManyField(
        'Tank',
    )
    engines = models.ManyToManyField(
        'Engine',
    )

    def __str__(self):
        return self.name



class Tank(models.Model):
    name = models.CharField(
        max_length=512,
        blank=True,
    )
    fuel = models.ForeignKey(
        'Fuel',
        models.CASCADE,
        null=True,
        blank=True,
    )
    capacity = models.DecimalField(
        max_digits=19,
        decimal_places=5,
        default=Decimal(0),
    )

    def __str__(self):
        if not self.name.strip():
            return f"{self.fuel} - {self.capacity}"

        return self.name
