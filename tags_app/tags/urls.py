from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'tags', views.TagViewSet)


urlpatterns = [
     path('', include(router.urls)),
     path('users_list/', views.get_users_list),
     path('user_tag/', views.get_user_tags), # you can provide <user_id> parameter
]
