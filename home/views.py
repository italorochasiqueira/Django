from django.shortcuts import render


def index(request):
    print('home')
    return render(
        request,
        'home/home.html'
    )

def exemplo1(request):
    print('pagina de exemplo')
    return render(
        request,
        'home/exemplo.html'
    )

