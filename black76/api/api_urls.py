from django.urls import include, path
from rest_framework import routers

from .api_views import ProductViewset, PricingViewset


router = routers.DefaultRouter()
router.register('products', ProductViewset)
router.register('pricing', PricingViewset)

urlpatterns = [
    path('', include(router.urls)),
]
