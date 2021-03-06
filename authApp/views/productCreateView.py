from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.serializers.productSerializer import ProductSerializer
import json

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)


        request_body=request.data['data']
        datos= json.loads(request_body)

        

        if valid_data['user_id'] != datos['user_id']:
            stringResponse = {'detail':'Acceso no autorizado - Creación de producto'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        if len(request.FILES) !=0:
            pro=request.FILES['audio']
            print(pro)

        set_data=datos['product_data']
        set_data['prod_urlproduct']=request.FILES['audio']
        set_data['prod_urlimagen']=request.FILES['imagen']

        serializer = ProductSerializer(data=set_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Producto creado", status=status.HTTP_201_CREATED)

