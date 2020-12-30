from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Story

def index(request):
    items = Story.objects.all()
    paginator = Paginator(items, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    return render(request, 'contact.html')


def story(request, slug):
    story = Story.objects.get(slug=slug)
    context = {'story' : story}
    return render(request, 'singlePost.html', context)