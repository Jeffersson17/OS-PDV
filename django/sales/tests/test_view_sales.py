from rest_framework import status
from rest_framework.test import APITestCase
from sales.models import Sales
from users.models import User


class SalesAPITestCase(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1",
            email="user1@user.com",
            password="user1",
        )
        self.user2 = User.objects.create_user(
            username="user2",
            email="user2@user.com",
            password="user2",
        )
        self.sale1 = Sales.objects.create(
            user=self.user1,
            purchase_date="2000-01-01",
        )
        self.url_api = "/sales/"
        self.url_list = "/sales-api/list/"
        self.url_detail = f"/sales-api/detail/{self.sale1.id}/"

    def test_create_sale(self):
        data_sale = {
            "user": self.user1.id,
            "purchase_date": "2006-02-12",
        }
        response = self.client.post(
            self.url_api, data_sale, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_api(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_api(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.sale1.id)
        self.assertEqual(response.data['purchase_date'], self.sale1.purchase_date)
        self.assertEqual(response.data['username'], self.user1.username)

    def test_update_detail_api(self):
        new_sale = {
            "user": self.user2.id,
            "purchase_date": "2001-03-02",
        }
        response = self.client.put(self.url_detail, new_sale, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.sale1.refresh_from_db()
        self.assertEqual(response.data['user'], new_sale['user'])
        self.assertEqual(response.data['purchase_date'], new_sale['purchase_date'])

    def test_delete_detail_api(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
