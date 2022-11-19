from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

data = {
    "blogs": [
        {
            'id': 1,
            'title': 'Komple Web Geliştirme',
            'image': 'foto1.jpg',
            'isActive': True,
            'isHome': True,
            'Description': 'Güzel Kurs'
        },
        {
            'id': 2,
            'title': 'Komple Mobil Geliştirme',
            'image': 'foto1.jpg',
            'isActive': True,
            'isHome': True,
            'Description': 'Güzel Kurs'
        },
        {
            'id': 3,
            'title': 'Komple Uygulama Geliştirme',
            'image': 'foto1.jpg',
            'isActive': True,
            'isHome': True,
            'Description': 'Güzel Kurs'
        },
        {
            'id': 4,
            'title': 'Komple Veri Geliştirme',
            'image': 'foto1.jpg',
            'isActive': False,
            'isHome': True,
            'Description': 'Güzel Kurs'
        }
    ]
}
def index(request):
    context = {
        "blogs": data['blogs']
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": data['blogs']
    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, id):
    return render(request, "blog/blogs-details.html", {
        'id': id,
    })
