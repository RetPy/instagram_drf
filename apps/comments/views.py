from rest_framework import viewsets

from .serializers import CommentSerializer
from .models import Comment


class CommentAPIView(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
