from django.db import models


class getempdetails(models.Model):
    EMPLOYEE_ID = models.IntegerField
    FIRST_NAME = models.CharField(max_length=100)
    LAST_NAME = models.CharField(max_length=100)
    EMAIL = models.CharField(max_length=100)