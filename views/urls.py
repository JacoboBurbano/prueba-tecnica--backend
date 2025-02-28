from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, ActivityViewSet, ProtectedView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'activities', ActivityViewSet, basename='activities')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/protected-view/', ProtectedView.as_view(), name='protected-view')
]