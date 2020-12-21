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

def work_with_own_tag_or_company_admin(action):
    def wrapper(request):
        user = request.user
        try:
            requested_user_id = int(request.query_params["user_id"])
        except:
            requested_user_id = user.id
        if user.id == requested_user_id:
            return action(user = user)
        else:
            if user.profile.is_company_admin:
                return action(user_id = requested_user_id)
            else:
                return Response({"error" : "Access forbidden"}, status = 403)
    wrapper.__name__ = action.__name__
    return wrapper

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

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@work_with_own_tag_or_company_admin
def get_user_tags(user = None, user_id = None):
    if user_id == None:
        profile = user.profile
        data = serializers.ProfileSerializer(profile).data
        return Response(data)
    # get profile by user_id
    try:
        profile = Profile.objects.get(user_id = user_id)
        data = serializers.ProfileSerializer(profile).data
        return Response(data)
    except:
        return Response({"error" : "UserDoesNotExist"}, status = 404)
