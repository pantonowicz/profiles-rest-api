from django.urls import path, include

from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register("hello-viewsets", views.HelloViewSet, basename='hello-viewset')
router.register("profiles", views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='hello-view'),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('', include(router.urls)),

]
