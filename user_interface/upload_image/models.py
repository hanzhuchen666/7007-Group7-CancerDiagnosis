from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Image(models.Model):
    username = models.CharField("用户名", max_length=30, unique=True)
    myfile = models.FileField(upload_to='images', default='')


    class Meta:
        db_table = "info"
