from django.db import models

# Create your models here.
class tbl_shops(models.Model):
    name=models.CharField(max_length=100)
    number=models.IntegerField()
    state=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    class Meta:
        db_table="tbl_shops"

