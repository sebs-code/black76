from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=255)

    GROUP_CHOICES = (
        ('Crude Oil and Refined Products', 'Crude Oil and Refined Products'),
        ('Natural Gas', 'Natural Gas'),
    )

    group = models.CharField(
        choices=GROUP_CHOICES,
        default='1',
        max_length=255
    )

    def __str__(self):
        return "{0} - {1}".format(self.code, self.name)


class Pricing(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    contract = models.CharField(max_length=255)
    last = models.FloatField()
    volume = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return "{0} - {1} - {2} - {3} - {4}".format(self.product.code, self.product.name, self.last, self.volume, self.date)

