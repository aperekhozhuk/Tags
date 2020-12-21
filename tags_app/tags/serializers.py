from rest_framework import serializers
from taggit.models import Tag
from .models import Profile


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    tags = TagSerializer(
        many = True,
        read_only = True,
    )

    class Meta:
        model = Profile
        fields = ['user_id', 'user_name', 'tags']
