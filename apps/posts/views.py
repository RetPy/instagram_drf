from rest_framework import viewsets

from .models import Post, PostImage
from .serializers import PostSerializer, PostImageSerializer


class PostAPIView(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostImageAPIView(viewsets.ModelViewSet):

    serializer_class = PostImageSerializer
    queryset = PostImage.objects.all()
