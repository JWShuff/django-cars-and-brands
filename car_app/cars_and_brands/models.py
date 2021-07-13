from django.db import models


class Brand(models.Model):
    pass


class Car(models.Model):
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    name = models.CharField(max_length=200)
    style = models.CharField(max_length=200)  # refactor to a category? SUV/Coupe/Etc?
