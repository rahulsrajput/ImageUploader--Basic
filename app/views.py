from django.shortcuts import render
from .models import ImageUploader

# Create your views here.
def home(request):
    all_obj = ImageUploader.objects.all()
    return render(request, 'home.html', context={'all_obj':all_obj})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')