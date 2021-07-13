from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"""
        Brand: {self.name}
        """


class Style(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"""
        Style: {self.type}
        """


class Car(models.Model):
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='cars')
    style = models.ForeignKey(
        Style,
        on_delete=models.CASCADE,
        related_name='cars')

    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"""
        Name: {self.name}
        {self.brand}
        {self.style}
        """