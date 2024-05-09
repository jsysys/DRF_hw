from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
class PostAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'complete', 'important']
        
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'important']

class PostDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['complete']        