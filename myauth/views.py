from django.shortcuts import render

# Create your views here.
from myauth.serializers import UserSerializer
from rest_framework import generics
from myauth.models import User

class UserView(generics.ListAPIView):
    """
    Returns a list of all authors.
    """
    model = User
    serializer_class = UserSerializer