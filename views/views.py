from rest_framework import viewsets, filters
from .models import CustomUser, Activity
from .serializer import UserSerializer, ActivitySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):  
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer 
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'phone', 'id']
    
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['action', 'timestamp']