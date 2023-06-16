from django.shortcuts import render, redirect
from .models import Cat


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cat = Cat.objects.create(name=name)
        return redirect('cat_stats')
    return render(request, 'cat/home.html')


def cat_stats(request):
    cat = Cat.objects.first()
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'feed':
            cat.feed()
        elif action == 'play':
            cat.play()
        elif action == 'sleep':
            cat.sleep()
    return render(request, 'cat/cat_stats.html', {'cat': cat})

