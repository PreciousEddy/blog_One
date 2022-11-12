from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        
        'author': 'PreciousCE',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Novemeber 1, 2022'
        
    },
    {
        
        'author': 'ChibuikePE',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Novemeber 2, 2022'
        
    },
    
    
    
    
    
]

# Create your views here
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogApp/home.html', context)

def about(request):
    return render(request, 'blogApp/about.html', {'title': 'About'})
