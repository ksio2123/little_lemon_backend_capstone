from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem, BookingItem
from .serializers import MenuSerializer, BookingSerializer


def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingItem.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
