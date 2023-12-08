from django.db import models

# Create your models here.


class Country(models.Model):
    country_id=models.IntegerField(primary_key=True)
    country_name=models.CharField(max_length=100)
    c_language=models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

class Capital(models.Model):
    capital_id=models.IntegerField()
    capital_name=models.CharField(max_length=100)
    country_id=models.OneToOneField(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.capital_name
