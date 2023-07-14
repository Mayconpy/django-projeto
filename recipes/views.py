from django.http import HttpResponse
from django.shortcuts import render

# from django.shortcuts import render


def my_view(request):
    return render(request, 'recipes/home.html', status=200, context={
        'nome': 'maycon'
    })


# Create your views here.


def contato(request):
    return render(request, 'temp.html')


def sobre(resquest):
    return HttpResponse('SOBRE')
