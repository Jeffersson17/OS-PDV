from addresses.models import Address, City
from enterprises.models import Enterprise
from products.models import Product, ProductBrand
from rest_framework import status
from rest_framework.test import APITestCase
from sales.models import ProductsSales, Sales
from users.models import User


class SalesAPITestCase(APITestCase):

    def setUp(self):
        self.city = City.objects.create(
            name="Fortaleza",
            state="CE",
        )
        self.address = Address.objects.create(
            address="Rua teste",
            city=self.city,
            cep="11111111",
            number="1066",
            complement="Sala teste",
        )
        self.enterprise = Enterprise.objects.create(
            name="Empresa teste",
            address=self.address,
            cnpj="52345778802125",
            area="Area teste",
        )
        self.product_brand = ProductBrand.objects.create(
            name="Teste",
        )
        self.product = Product.objects.create(
            name="Teste",
            price="109.99",
            enterprise=self.enterprise,
            mark=self.product_brand,
            stock=20,
        )
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
        self.sale2 = Sales.objects.create(
            user=self.user2,
            purchase_date="2000-01-28",
        )
        self.product_sale1 = ProductsSales.objects.create(
            product=self.product,
            sale=self.sale1,
            quantity_purchased=1,
        )
        self.url_produt_sale_api = "/products_sales/"
        self.url_sale_api = "/sales/"
        self.url_sale_detail = f"/sales-api/detail/{self.sale1.id}/"
        self.url_detail_products_sales = (
            f"/products-sales/detail/{self.product_sale1.id}/"
        )

    def test_create_sale(self):
        data_sale = {
            "user": self.user1.id,
            "purchase_date": "2006-02-12",
        }
        response = self.client.post(
            self.url_sale_api, data_sale, format="json"
        )
        response_list = self.client.get(self.url_sale_api)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_list.status_code, status.HTTP_200_OK)

    def test_detail_api_sale(self):
        response = self.client.get(self.url_sale_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.sale1.id)
        self.assertEqual(
            response.data["purchase_date"], self.sale1.purchase_date
        )
        self.assertEqual(response.data["username"], self.user1.username)

    def test_update_detail_api_sale(self):
        new_sale = {
            "user": self.user2.id,
            "purchase_date": "2001-03-02",
        }
        response = self.client.put(
            self.url_sale_detail, new_sale, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sale1.refresh_from_db()
        self.assertEqual(response.data["user"], new_sale["user"])
        self.assertEqual(
            response.data["purchase_date"], new_sale["purchase_date"]
        )

    def test_delete_detail_api_sale(self):
        response = self.client.delete(self.url_sale_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_product_sale(self):
        data_product_sale = {
            "product": self.product.id,
            "sale": self.sale1.id,
            "quantity_purchased": 1,
        }
        response = self.client.post(
            self.url_produt_sale_api, data_product_sale, format="json"
        )
        response_list = self.client.get(self.url_produt_sale_api)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_list.status_code, status.HTTP_200_OK)

    def test_update_product_sale_api(self):
        new_data_product_sale = {
            "product": self.product.id,
            "sale": self.sale2.id,
            "quantity_purchased": 2,
        }
        response = self.client.put(
            self.url_detail_products_sales,
            new_data_product_sale,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product_sale1.refresh_from_db()
        self.assertEqual(response.data["product"], self.product.id)
        self.assertEqual(response.data["sale"], self.sale2.id)

    def test_delete_product_sale_api(self):
        response = self.client.delete(self.url_detail_products_sales)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
