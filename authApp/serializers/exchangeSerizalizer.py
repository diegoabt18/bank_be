from authApp.models.user import User
from authApp.models.product import Product
from authApp.models.exchange import Exchange
from rest_framework import serializers

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ['exch_id', 'exch_userorigin_id', 'exch_userdestination_id', 'exch_prod_id', 'exch_fecha']


    def to_representation(self, obj):
        exchange = Exchange.objects.get(exch_id=obj.exch_id)
        return {
            "exch_id" : exchange.exch_id, 
            "exch_userorigin_id" : exchange.exch_userorigin_id, 
            "exch_userdestination_id" : exchange.exch_userdestination_id, 
            "exch_prod_id" : exchange.exch_prod_id, 
            "exch_fecha" : exchange.exch_fecha
        }




        