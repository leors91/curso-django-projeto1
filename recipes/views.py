from django.shortcuts import render
from django.http import HttpResponse


# def home(request):
#     return HttpResponse('''<!DOCTYPE>
#     <html>
#     <head><title>Olá mundo</title></head>

#     <body>
#         <h1>Olá mundo</h1>
#     <body>


#     </html>
#     ''')

def home(request):
    return render(request, 'recipes/home.html')

def contato(request):
    return HttpResponse('contato 40')

def sobre(request):
    return HttpResponse('sobre 30')