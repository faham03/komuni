from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import  Post,Comment, Resource
from django.shortcuts import render
from .serializers import RegisterSerializer, PostSerializer, CommentSerializer, ResourceSerializer
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            raise PermissionDenied("Vous ne pouvez modifier que vo propres posts.")
        serializer.save()

class PostDeleteView(generics.DestroyAPIView):
        queryset = Post.objects.all()
        serializer_class = PostSerializer
        permission_classes = [permissions.IsAuthenticated]

        def perform_destroy(self, instance):
            if self.request.user != instance.author:
                raise PermissionDenied("Vous ne pouvez supprimer que vos propres posts.")
            instance.delete()

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(author=self.request.user, post_id=post_id)

class CommentUpdateView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            raise PermissionDenied("Vous ne pouvez modifier que vos propres commentaires.")
        serializer.save()

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied("Vous ne pouvez supprimer que vos propres commentaires.")
        instance.delete()

class ResourceListCreateView(generics.ListCreateAPIView):
    queryset = Resource.objects.all().order_by('-created_at')
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ResourceDeleteView(generics.DestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied("Vous ne pouvez supprimer que vos propres ressources.")
        instance.delete()