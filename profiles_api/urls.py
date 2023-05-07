from django.urls import path, include
from .views import HelloApiView, HelloViewSet, UserProfileViewset, UserLoginApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
router.register('profile', UserProfileViewset) 

urlpatterns = [
    path('hello/', HelloApiView.as_view(), name='HelloApiView'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('', include(router.urls)),
]