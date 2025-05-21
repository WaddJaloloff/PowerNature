from django.shortcuts import render
from .models import Post, OurWorks, Savollar


def index(request):
    posts = Post.objects.all()
    ourworks = OurWorks.objects.all()
    faqs = Savollar.objects.all()
    context = {
        "posts": posts, 
        "ourworks": ourworks, 
        "faqs": faqs}
    return render(request, "index.html", context)
