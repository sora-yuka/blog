from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from applications.post.models import Post
from applications.post.serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import *
from applications.post.permissions import IsOwner

# class PostAPIView(ViewSet):
#     def list(self, request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=HTTP_201_CREATED)
        

#* Способ 2 - ModelViewSet        
class PostAPIView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]
    