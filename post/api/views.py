from rest_framework.exceptions import ValidationError
from post.api.serializers import PostSerializer, CommentSerializer
from post.models import PostTable, CommentTable

from rest_framework import generics

class PostList(generics.ListAPIView):
    queryset = PostTable.objects.all()
    serializer_class = PostSerializer

class PostCreate(generics.CreateAPIView):
    queryset = PostTable.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostTable.objects.all()
    serializer_class = PostSerializer
    
class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    
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