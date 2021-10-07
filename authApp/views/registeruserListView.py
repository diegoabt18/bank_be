from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response
from authApp.models.register_user import Register_user
from rest_framework.permissions import IsAuthenticated
from authApp.serializers.registeruserSerializer import RegisteruserSerealizer

class RegisteruserListView(views.APIView):
    queryset = Register_user.objects.all()
    serializer_class = RegisteruserSerealizer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = self.get_queryset()
        serializer = RegisteruserSerealizer(queryset, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)
