from rest_framework import viewsets

from .serializers import TagSerializer
from .models import Tag


class TagAPIView(viewsets.ModelViewSet):

    serializer_class = TagSerializer
    queryset = Tag.objects.all()
