from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.product import Product
from authApp.serializers.productSerializer import ProductSerializer
from django.core import serializers
from django.http import HttpResponse

class ProductUserListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        print("***********************************")
        print(valid_data['fields'])
        print("***********************************")
        print(valid_data['fields']['prod_user'])


        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Acceso no autorizado - Lista de elementos'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Product.objects.filter(prod_user_id=self.kwargs['user'])
        print("***********************************")
        print(queryset)
        allProductsByUSer = serializers.serialize("json", queryset)
        print("***********************************")
        print(allProductsByUSer)


        [{"model": "authApp.product", "pk": 29, "fields": {"prod_user": 1, "prod_name": "product", "prod_artist": "artist", "prod_genre": "genre", "prod_rate": 5, "prod_type": "type", "prod_description": "descr", "prod_urlproduct": "audio/EL_LEON_Y_EL_MOSQUITO.mp4", "prod_urlimagen": "imagen/titeres.jpg", "prod_state": false}}]

        {
            "user_id": 3,
            "product_data": {
                "prod_user": 3, 
                "prod_name": "1111ot gonna take it", 
                "prod_artist": "2222Twisted Sister", 
                "prod_genre":"Rock1111",
                "prod_rate": 5,  
                "prod_type": "CD",
                "prod_description": "Stay hungry3333654",
                "prod_urlproduct": "rulproducto",
                "prod_urlimagen": "urlimagen",
                "prod_state" : false
            }
        }


        # return queryset
        return HttpResponse(allProductsByUSer, content_type='application/json')


