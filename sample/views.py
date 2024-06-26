from rest_framework import viewsets
from .models import InvoiceHeader
from .serializers import InvoiceHeaderSerializer

class InvoiceHeaderViewSet(viewsets.ModelViewSet):
    queryset = InvoiceHeader.objects.all()
    serializer_class = InvoiceHeaderSerializer
