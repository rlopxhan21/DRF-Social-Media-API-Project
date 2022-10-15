from rest_framework.exceptions import ValidationError
from post.api.serializers import PostSerializer, CommentSerializer
from post.models import PostTable, CommentTable

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permission import IsOwnerorReadOnlyorAdmin
from .pagination import LargeResultPagination
from rest_framework.throttling import AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend

class PostList(generics.ListAPIView):
    queryset = PostTable.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post_desc', 'author__username']


class PostCreate(generics.CreateAPIView):
    queryset = PostTable.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostTable.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerorReadOnlyorAdmin]
    
class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = LargeResultPagination
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        postinstance =  PostTable.objects.get(pk=pk)
        return CommentTable.objects.filter(post_ref=postinstance)

class CommentCreate(generics.CreateAPIView):
    queryset = CommentTable.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        postinstance = PostTable.objects.filter(pk=pk)
        
        if postinstance.exists():
            if serializer.is_valid():
                serializer.save(post_ref_id=pk, author=self.request.user)
                
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentTable.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerorReadOnlyorAdmin]

    