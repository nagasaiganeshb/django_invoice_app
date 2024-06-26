from django.contrib import admin
from .models import InvoiceBillSundry, InvoiceHeader, InvoiceItem

admin.site.register(InvoiceBillSundry)
admin.site.register(InvoiceHeader)
admin.site.register(InvoiceItem)