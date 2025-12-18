from django.shortcuts import render
from .models import BlogPost, Project
from .serializers import BlogPostSerializer, ProjectSerializer
from rest_framework import viewsets, permissions, decorators
from rest_framework.decorators import action
from rest_framework.response import Response

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True #if the request from the user is a get, we allow this, its a "safe method"
        return request.user and request.user.is_staff #If the request is not one of those safe methods, 
    #we are first checking that the user exists, and then the value of is_staff

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer 
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False, methods=['get'])
    def latest(self, request):
        post = self.queryset.filter(status='published').order_by('-published_at').first()
        # We filter the queryset that we set on line 16. filter is an sql where clause. order_by is an sql order by. the minus sign denotes Descending.
        # dot first gets the first one of this set.
        serializer = self.get_serializer(post)
        return Response(serializer.data)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]