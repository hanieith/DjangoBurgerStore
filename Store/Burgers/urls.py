from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('search/', Search.as_view(), name='search'),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    #path('api/v1/postlist/', PostApiView.as_view()),
    #path('api/v1/postlist/<int:pk>', OnePostApiView.as_view()),
    path('api/v1/', include(router.urls)),
]
