from django.test import TestCase, Client
from .models import CustomUser, Activity
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
# Create your tests here.
class UserAuthTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="TestUser",
            email="test@example.com",
            password="securepassword",
            is_active=True
        )
        self.token_url = "/views/api/token/"
        self.protected_url = "/views/api/token/protected-view/"
        refresh = RefreshToken.for_user(self.user)
        self.access_token = refresh.access_token
    
    def test_get_token_jwt(self):
        response = self.client.post(self.token_url, {
            "username" : "TestUser", 
            "email" : "test@example.com",
            "password" : "securepassword" 
        })
        print(response.json())
        self.assertEqual(response.status_code, 200)
        
    def test_get_protected_token(self):
        response = self.client.post(self.token_url, {
            "username" : "TestUser",
            "email" : "test@example.com",
            "password" : "securepassword" 
        })
        token = response.data['access']
        protected_response = self.client.get(
            self.protected_url,
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )
        self.assertEqual(protected_response.status_code, 200)
    
    def test_get_auth_user(self):
        response = self.client.get(
            '/views/api/users/?email=test@example.com',
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
            )
        print(response)
        self.assertEqual(response.status_code, 200)
        
        