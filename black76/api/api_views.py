from rest_framework import viewsets

from .models import Product, Pricing
from .serializers import ProductSerializer, PricingSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PricingViewset(viewsets.ModelViewSet):
    queryset = Pricing.objects.all().order_by('-date')
    serializer_class = PricingSerializer

    def get_queryset(self):
        code = self.request.query_params.get('code')
        if code:
            return self.queryset.filter(product__code=code)
        else:
            return self.queryset
