from django.shortcuts import render
from .models import BlogPost, Project
from .serializers import BlogPostSerializer, ProjectSerializer
from rest_framework import viewsets, permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True #if the request from the user is a get, we allow this, its a "safe method"
        return request.user and request.user.is_staff #If the request is not one of those safe methods, 
    #we are first checking that the user exists, and then the value of is_staff

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer #todo, make serializers
    permission_classes = [IsAdminOrReadOnly]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]