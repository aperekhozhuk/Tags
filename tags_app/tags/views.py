from rest_framework import permissions, viewsets
from taggit.models import Tag
from .models import Profile
from . import serializers


class TagsPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        authenticated = permissions.IsAuthenticated.has_permission(self, request, view)
        if request.method == "GET":
            return authenticated
        return authenticated and request.user.profile.is_customer_admin

class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = [TagsPermission]
