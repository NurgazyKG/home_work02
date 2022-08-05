from django.db import models

# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    Speed = models.IntegerField()
    Year = models.DateField()

    def __str__(self):
        return self.name