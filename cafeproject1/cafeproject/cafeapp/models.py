from django.db import models
from django.db.models import CharField


# Create your models here.
class food(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()
    # po=models.CharField(max_length=250)

    def __str__(self):
        return self.name


