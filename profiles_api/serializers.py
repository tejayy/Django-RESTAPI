from rest_framework import serializers


class UserProfileSerializer(serializers.Serializer):
    """Serializer a name field for testing out APIviews"""
    name  = serializers.CharField(max_length=10)
    

