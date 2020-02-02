from django.db import models

class Borough(models.Model):
    name = models.CharField(max_length=50)
    borough_Main_Img = models.ImageField(upload_to='images/')
