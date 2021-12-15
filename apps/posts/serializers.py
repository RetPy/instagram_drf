from rest_framework import serializers

from .models import Post, PostImage


class PostImageSerializer(serializers.ModelSerializer):

    class Meta:

        model = PostImage
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    post_image = PostImageSerializer(
        many=True,
        read_only=True
    )
    user = serializers.CharField(read_only=True)

    class Meta:

        model = Post
        fields = '__all__'
        