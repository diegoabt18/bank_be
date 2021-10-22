from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.serializers.productSerializer import ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)
        print("++++++++++++++++++++++++++++++++++++++++++++++")
        valores=request.data['data']
        print(valores)
        valores2=valores['product_data']
        print(valores2)
        valores3=valores2['prod_user']
        print(valores3)

        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail':'Acceso no autorizado - Creación de producto'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        if len(request.FILES) !=0:
            pro=request.FILES['img']
            print(pro)
        serializer = ProductSerializer(data=request.data['product_data'])

        


        print({**request.POST,**request.FILES})
        datos = request.data['product_data']
        filea =datos["prod_urlimagen"]
        fileb = datos['prod_urlproduct']
        print("##################################################")
        print(filea)
        print("##################################################")
        print(fileb)
        print("##################################################")
   
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Producto creado", status=status.HTTP_201_CREATED)

