from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserViewSetTestCase(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1",
            email="user1@user.com",
            password="user1",
        )
        self.url = "/users/"
        self.url_detail = f"/users-api/detail/{self.user1.id}/"

    def test_api_view_user(self):
        payload = {
            "username": "teste",
            "email": "teste@teste.com",
            "password": "teste",
            "phone_number": "85986882954",
            "cpf": "00100100101",
            "date_birth": "2000-01-01",
        }
        response_list = self.client.get(self.url)
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_list.status_code, status.HTTP_200_OK)

    def test_detail_api(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.user1.id)
        self.assertEqual(response.data["username"], self.user1.username)
        self.assertEqual(response.data["email"], self.user1.email)
        self.assertTrue(self.user1.check_password("user1"))

    def test_update_detail_api(self):
        new_payload = {
            "username": "new_teste",
            "email": "new_teste@teste.com",
            "password": "new_teste",
            "phone_number": "85986882955",
            "cpf": "00100100102",
            "date_birth": "2006-12-02",
        }
        response = self.client.put(self.url_detail, new_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user1.refresh_from_db()
        self.assertEqual(self.user1.username, new_payload["username"])
        self.assertEqual(self.user1.email, new_payload["email"])
        self.assertEqual(self.user1.phone_number, new_payload["phone_number"])
        self.assertEqual(self.user1.cpf, new_payload["cpf"])
        self.assertEqual(str(self.user1.date_birth), new_payload["date_birth"])

    def test_delete_detail_api(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
