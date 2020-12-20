from rest_framework import serializers
from taggit.models import Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']
