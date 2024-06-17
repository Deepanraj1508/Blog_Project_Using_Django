from django.urls import path, re_path
from .views import BlogPostListCreateAPIView, BlogPostDetailAPIView, BlogPostUpdateAPIView, BlogPostDeleteAPIView

urlpatterns = [
    path('', BlogPostListCreateAPIView.as_view(), name='blogpost-list-create'),
    re_path(r'^(?P<pk>\d+)/$', BlogPostDetailAPIView.as_view(), name='blogpost-detail'),
    re_path(r'^(?P<pk>\d+)/update/$', BlogPostUpdateAPIView.as_view(), name='blogpost-update'),
    re_path(r'^(?P<pk>\d+)/delete/$', BlogPostDeleteAPIView.as_view(), name='blogpost-delete'),
]
