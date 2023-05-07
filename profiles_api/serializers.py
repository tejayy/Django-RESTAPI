from rest_framework import serializers
from .models import UserProfile

class HelloSerializers(serializers.Serializer):
    """Serializer a name field for testing out APIviews"""
    name  = serializers.CharField(max_length=10)
    

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a user profile object"""
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }
        
    def create(self, validated_data):
        """Create and return a new user profile"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
            
        )
        return user

