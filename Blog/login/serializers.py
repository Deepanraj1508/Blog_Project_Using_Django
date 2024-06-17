# serializers.py
from rest_framework import serializers # type: ignore
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'name', 'image', 'video', 'description']
