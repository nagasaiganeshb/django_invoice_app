from .models import InvoiceHeader, InvoiceItem, InvoiceBillSundry
from rest_framework import serializers

class InvoiceItemSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    amount = serializers.ReadOnlyField()

    class Meta:
        model = InvoiceItem
        fields = "__all__"
        # fields = ('item_name', 'quantity', 'price', 'amount')

class InvoiceBillSundrySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = InvoiceBillSundry
        fields = "__all__"

class InvoiceHeaderSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    items = InvoiceItemSerializer(many=True)
    bill_sundry = InvoiceBillSundrySerializer(many=False)

    class Meta:
        model = InvoiceHeader
        fields = "__all__"
    
    def create(self, validated_data):
        items = validated_data.get('items', [])
        if not items:
            raise serializers.ValidationError("items should not be empty.")
        
        total = 0
        for item in items:
            item['amount'] = item.get('quantity') * item.get('price')
            total += item['amount']
            if item['amount'] <= 0:
                raise serializers.ValidationError("amount should be greater than zero.")
        
        total += validated_data['bill_sundry']['amount']

        return InvoiceHeader.objects.create(**validated_data)
