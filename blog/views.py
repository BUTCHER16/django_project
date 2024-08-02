from django.shortcuts import render

# Create your views here.

posts = [
    {
    'author' : 'Jane Doe',
    'title' : 'Blog Post 1',
    'content' : 'This is the First Post',
    'date_posted' : 'Aug 28, 2022'
    },
    {
    'author' : 'Albert Ravidoss',
    'title' : 'Blog Post 2',
    'content' : 'This is the Second Post',
    'date_posted' : 'Aug 28, 2022'
    }
    
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})