from .models import Post
from .serializers import PostSerializer, PostAllSerializer, PostCreateSerializer, PostDoneSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Post의 목록을 보여주는 역할
class TodoList(APIView):
    # Post list를 보여줄 때
    def get(self, request):
        posts = Post.objects.filter(complete=False)
        serializer = PostAllSerializer(posts, many=True)
        return Response()

    # 새로운 Post를 작성할 때
    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Post의 detail을 보여주는 역할
class TodoDetail(APIView):
    # Post 객체 가져오기
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
        
    # Post의 detail 보기
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # Post 수정하기
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostCreateSerializer(post, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoneList(APIView):
    def get(self, request):
        posts = Post.objects.filter(complete=True)
        serializer = PostAllSerializer(posts, many=True)
        return Response()

class DoneTodo(APIView): 
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostDoneSerializer(post, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    