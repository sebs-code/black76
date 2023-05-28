from django.contrib import admin

# Register your models here.
from .models import Pricing, Product

admin.site.register(Product)
admin.site.register(Pricing)
