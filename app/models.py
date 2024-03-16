from django.db import models

# Create your models here.
class ImageUploader(models.Model):
    image = models.ImageField(upload_to='02_image_uploader/images')