from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from .serializers import HelloSerializers, UserProfileSerializer, ProfileFeedItemSerializer
from .models import UserProfile, ProfileFeedItem
from .permissions import UpdateOwnProfile, UpdateOwnStatus


"""Create your views here."""

class HelloApiView(APIView):
    """Test API view"""
    serializer_class = HelloSerializers
    
    def get(self, request):
        """Returns a list of API Views Features"""
        an_apiview = [
            'uses Http method as funtions(get, post, put, delete)',
            'Is similar to traditional Django views',
            'Gives you the most control over the application logic',
            "is Mapped manually to urls", 
        ]

        return Response(
            {
                'message': 'Hello!',
                'an_apiview': an_apiview
            }
        )
        
    def post(self, request):
        """Create a Hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello! {name}'
            return Response(
                {
                    'message': message
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        """Handle Updating objects"""
        return Response(
            {
                'method': 'PUT',
            }
        )
        
    def patch(self, request, pk=None):
        """Handle a partial update of a object"""
        return Response(
            {
                'method': 'PATCH',
            }
        )
        
    def delete(self, request, pk=None):
        """Delete Request"""
        return Response(
            {
                'methods': 'Delete',
            }
        )
        
        
class HelloViewSet(viewsets.ViewSet):
    """Test Api ViewSet"""
    serializer_class = HelloSerializers
    
    def list(self, request):
        """Return a Hello Message"""
        a_viewset = [
            'Uses action  (list,create, retrive, update, partial update)',
            'Automatically maps to urls Routers',
            'Provides more functionality with less code',
        ]
        return Response(
            {
                'message': 'Hello Message',
                'a_viewset': a_viewset
            }
        )
        
    
    def create(self, request):
        """Create a new Hello Message"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response(
                {
                    'message': message
                }
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def retrieve(self, request, pk=None):
        """Handle GET requests getting object by id"""
        return Response(
            {
                'httpMethod': 'GET',
            }
        )
        
    def update(self, request, pk=None):
        """Update object"""
        return Response(
            {
                'httpMethod': 'PUT',
            }
        )
        
    def partial_update(self, request, pk=None):
        """Handle updating a partial of object"""
        return Response(
            {
                'httpMethod': 'PATCH',
            }
        )
        
    def delete(self, request, pk=None):
        """Delete a object"""
        return Response(
            {
                'httpMethod': 'DELETE',
            }
        )
        
        
class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating users profile"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)    
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    

class UserLoginApiView(ObtainAuthToken):
    '''Handle creating and updating users'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class UserProfileFeedViewset(viewsets.ModelViewSet):
    '''Handle creating and updating profile fields items'''
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (UpdateOwnStatus, IsAuthenticated)
    
    def perform_create(self, serializer):
        '''Sets the User Profile to the logged in user'''''
        serializer.save(user_profile=self.request.user)