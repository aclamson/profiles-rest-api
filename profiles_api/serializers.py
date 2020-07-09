from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    # define the types of serializers you want to accept
    # take care of validation rules
    name = serializers.CharField(max_length=10)
    