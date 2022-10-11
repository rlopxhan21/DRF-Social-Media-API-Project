from post.models import PostTable, CommentTable

from rest_framework import serializers

        
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post_ref = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = CommentTable
        fields = "__all__"
        
        
class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    availablecomment = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = PostTable
        fields = '__all__'
        