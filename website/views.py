from django.shortcuts import render
from .models import Post  # Assuming you have a Post model defined in models.py


def home(request):
    posts = Post.objects.all()  # or your custom list
    return render(request, 'home.html', {'posts': posts})


def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def category(request, category_name):
    return render(request, 'category.html', {'category_name': category_name})

def single_post(request, post_id):
    return render(request, 'single-ost.html', {'post_id': post_id})


# Create your views here.
