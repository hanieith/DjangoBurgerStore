from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk','slug', 'title', 'author', 'category', 'created_at', 'tags', 'content')