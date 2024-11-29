from django.db import models


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=250)
    cep = models.CharField(max_length=8)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()


    def __str__(self):
        return self.address
