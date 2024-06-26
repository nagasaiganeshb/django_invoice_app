from django.db import models

class InvoiceItem(models.Model):
    id = models.IntegerField(primary_key=True)
    item_name = models.CharField(null=False, max_length=255)
    quantity = models.FloatField()
    price = models.FloatField()
    amount = models.FloatField()

class InvoiceBillSundry(models.Model):
    id = models.IntegerField(primary_key=True)
    bill_sundry_name = models.CharField(null=False, max_length=255)
    amount = models.FloatField()

class InvoiceHeader(models.Model):
    id = models.IntegerField(primary_key=True)
    items = models.ManyToManyField(InvoiceItem)
    bill_sundry = models.ForeignKey(InvoiceBillSundry, on_delete=models.CASCADE)
    date = models.DateTimeField()
    invoice_number = models.IntegerField(null=False)
    customer_name = models.CharField(null=False, max_length=255)
    billing_address = models.CharField(null=False, max_length=255)
    shipping_address = models.CharField(null=False, max_length=255)
    gstin = models.CharField(null=False, max_length=255)
    total_amount = models.FloatField()
