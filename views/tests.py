from django.test import TestCase, Client
from .models import CustomUser, Activity

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        CustomUser.objects.create_user(
            username="Test User",
            email="test@example.com",
            phone="1234567890",
            password="securepassword"
        )
        
    def get_user(self):
        response = self.client.get('/views/api/users/?username=Manuel')
        print({'response': response.json()})
        self.assertEqual(response.status_code, 200)
        
        