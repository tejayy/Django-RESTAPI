from django.urls import path, include
from .views import HelloApiView, HelloViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')


urlpatterns = [
    path('hello/', HelloApiView.as_view(), name='HelloApiView'),
    path('', include(router.urls)),
]