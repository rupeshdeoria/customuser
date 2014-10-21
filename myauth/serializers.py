#from django.core import serializers
from rest_framework import serializers
from myauth.models import User
class UserSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """
    class Meta:
        model = User
        fields = ('email','date_joined')