from django.shortcuts import render

rounds = [
    {
        'golfer': 'Wil',
        'course': 'Marshfield CC',
        'total_strokes_gained': -2.5,
        'date_posted': 'May 6, 2024',
    },
    {
        'golfer': 'Wil',
        'course': 'Marshfield CC',
        'total_strokes_gained': -7,
        'date_posted': 'May 15, 2024',
    }
]

def home(request):
    context = {'rounds': rounds}
    # this render takes in a request, and 'directory within local templates dir/page to load'
    return render(request, 'golf_round_post/home.html', context)


def about(request):
    return render(request, 'golf_round_post/about.html', {'title': 'About'})
