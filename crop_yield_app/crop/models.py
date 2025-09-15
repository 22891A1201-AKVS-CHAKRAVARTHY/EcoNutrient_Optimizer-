from django.db import models

class CropInput(models.Model):
    crop_name = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=100)

    def __str__(self):
        return self.crop_name
