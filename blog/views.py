from django.shortcuts import render

posts = [
    {
        'author': 'Alireza',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'May 16, 2020'
    },
    {
        'author': 'Reza',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'May 17, 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
