from django.shortcuts import render
from django.http import HttpResponse

posts = [{
    'author': 'Usman Malik',
    'title': 'Blog Post 1',
    'content': 'First Post content',
    'date_posted': 'May 17, 2020'
}, {
    'author': 'Usman Malik',
    'title': 'Blog Post 1',
    'content': 'First Post content',
    'date_posted': 'May 17, 2020'
}
]


# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
