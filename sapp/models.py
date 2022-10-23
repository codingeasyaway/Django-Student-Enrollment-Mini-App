from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    sclass = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return self.name