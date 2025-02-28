from rest_framework import viewsets, filters
from .models import CustomUser, Activity
from .serializer import UserSerializer, ActivitySerializer
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.response import Response
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

class UserViewSet(viewsets.ModelViewSet):  
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer 
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'phone', 'id']
    
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['action', 'timestamp']