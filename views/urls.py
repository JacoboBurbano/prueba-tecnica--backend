from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ActivityViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'activities', ActivityViewSet, basename='activities')

urlpatterns = [
    path('api/', include(router.urls)),
]