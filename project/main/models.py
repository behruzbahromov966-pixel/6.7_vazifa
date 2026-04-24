from django.db import models

# Create your models here.
class Brend(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Pk: {self.pk}, Name: {self.name}"


class Car(models.Model):
    name = models.CharField(max_length=100)
    manufacture_year = models.DateField()
    car_owner = models.CharField(max_length=100)
    car_number = models.CharField(max_length=20)
    owner_number = models.CharField(max_length=15)
    brand = models.ForeignKey(Brend, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.car_number}"

    def __repr__(self):
        return (f"Pk: {self.pk}, Name: {self.name}, Manufacture year: {self.manufacture_year}, Car number: {self.car_number},"
                f"Owner: {self.car_owner}, Owner number: {self.owner_number}")