from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import BlogPost
from .serializers import BlogPostSerializer
from drf_yasg.utils import swagger_auto_schema

class BlogPostListCreateAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve a list of all blog posts",
        operation_id="listBlogPosts",
        responses={200: BlogPostSerializer(many=True)},
        tags=["Blog Posts"]
    )
    def get(self, request):
        blog_posts = BlogPost.objects.filter(is_deleted=False)
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new blog post",
        operation_id="createBlogPost",
        request_body=BlogPostSerializer,
        responses={
            201: BlogPostSerializer,
            400: 'Bad Request'
        },
        tags=["Blog Posts"]
    )
    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogPostDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk, is_deleted=False)
        except BlogPost.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Retrieve a specific blog post by ID",
        operation_id="getBlogPost",
        responses={
            200: BlogPostSerializer,
            404: 'Not Found'
        },
        tags=["Blog Posts"]
    )
    def get(self, request, pk):
        blog_post = self.get_object(pk)
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)

class BlogPostUpdateAPIView(APIView):

    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk, is_deleted=False)
        except BlogPost.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Update a specific blog post by ID",
        operation_id="updateBlogPost",
        request_body=BlogPostSerializer,
        responses={
            200: BlogPostSerializer,
            400: 'Bad Request',
            404: 'Not Found'
        },
        tags=["Blog Posts"]
    )
    def put(self, request, pk):
        blog_post = self.get_object(pk)
        serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogPostDeleteAPIView(APIView):

    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk, is_deleted=False)
        except BlogPost.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Soft delete a specific blog post by ID",
        operation_id="deleteBlogPost",
        responses={
            204: 'No Content',
            404: 'Not Found'
        },
        tags=["Blog Posts"]
    )
    def delete(self, request, pk):
        blog_post = self.get_object(pk)
        blog_post.is_deleted = True
        blog_post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
