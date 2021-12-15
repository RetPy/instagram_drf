from django.db import models

from apps.users.models import User
from apps.posts.models import Post


class Comment(models.Model):

    text = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comment_post'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comment_user'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='comments_comment',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.text}'
