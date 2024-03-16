from django.contrib import admin
from .models import ImageUploader
# Register your models here.

@admin.register(ImageUploader)
class ImageUploaderAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']