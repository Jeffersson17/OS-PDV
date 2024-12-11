from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from users.models import User


class UserViewSetTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = "/users/"
        self.user1 = User.objects.create_user(
            username="teste1",
            email="teste1@teste.com",
            password="teste1",
        )

    def test_create_user(self):
        self.data = {"username": "teste", "password": "teste"}
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_user(self):
        self.url_list = "/users-api/list/"
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
