from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from taggit.models import Tag
from .models import Profile
from django.contrib.auth.models import User
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


class IsCustomerAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.profile.is_customer_admin

@api_view(['GET'])
@permission_classes([IsCustomerAdmin])
def get_users_list(request):
    users = User.objects.all()
    data = [
        {
            "id" : user.id,
            "username" : user.username,
        } for user in users
    ]
    return Response(data)
