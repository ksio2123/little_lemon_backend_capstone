from rest_framework import serializers
from .models import MenuItem, BookingItem
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingItem
        fields = ['id', 'name', 'no_of_guests', 'booking_date']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['username', 'email', 'id', 'groups']