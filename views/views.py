from rest_framework import viewsets, filters
from .models import CustomUser, Activity
from .serializer import UserSerializer, ActivitySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': 'You have access'})

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated] 
    
    def get(self, request):
        return Response({"message": "You have access"})

class UserViewSet(viewsets.ModelViewSet):  
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer 
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
    
    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "phone": user.phone,
        })
    
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['action', 'timestamp']