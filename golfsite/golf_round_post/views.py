from django.shortcuts import render
from .models import GolfRound

def home(request):
    context = {
        'posts': GolfRound.objects.all()
    }

    # this render takes in a request, and 'directory within local templates dir/page to load'
    return render(request, "golf_round_post/home.html", context)


def about(request):
    return render(request, "golf_round_post/about.html", {"title": "About"})
