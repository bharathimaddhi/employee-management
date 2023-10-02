from django.db import models
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phoneNo = models.CharField(max_length=20)
    addressDetails = models.JSONField()
    workExperience = models.JSONField()
    qualifications = models.JSONField()
    projects = models.JSONField()
    photo = models.TextField()

    def _str_(self):
        return self.name

