from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.product import Product
from authApp.serializers.productSerializer import ProductSerializer
import json

class ProductUpdateView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Product.objects.all()

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        request_body=request.data['data']
        datos= json.loads(request_body)
        print(datos)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Acceso no autorizado - Actualización producto'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        if len(request.FILES) !=0:
            pro=request.FILES['audio']
            print(pro)

        #set_data=datos['product_data']
        datos['prod_urlproduct']=request.FILES['audio']
        datos['prod_urlimagen']=request.FILES['imagen']
        print(datos)
        request.data=datos

        return super().update(request, *args, **kwargs)


