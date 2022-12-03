from django.shortcuts import render

from .models import Project

def index(request):
    posts = Project.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'portfolio/index.html', context=context)