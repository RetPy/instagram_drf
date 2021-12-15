from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserAPIView(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()


@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.date)
