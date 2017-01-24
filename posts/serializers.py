from rest_framework import serializers
from posts.models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'content','tags')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts= serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'posts')