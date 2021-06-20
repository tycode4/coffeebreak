from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=20, null = True, blank = True)
	price = models.IntegerField()
	description = models.CharField(max_length=20, null=True, blank=True)

	class Meta:
		db_table = "products"
