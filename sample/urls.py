
from django.urls import include, path
from rest_framework import routers
from .views import InvoiceHeaderViewSet

router = routers.DefaultRouter()
router.register(r'invoices', InvoiceHeaderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]