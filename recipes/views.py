from django.shortcuts import render
from django.http import HttpResponse

# render vai renderizar o arquivo html 

# def home(request):
#     return HttpResponse('''<!DOCTYPE>
#     <html>
#     <head><title>Olá mundo</title></head>

#     <body>
#         <h1>Olá mundo</h1>
#     <body>


#     </html>
#     ''')

# fazer a requisicao dos templates com namespace para não confundor com base_templates
def home(request):
    return render(request, 'recipes/home.html', context={'name':'Leomnardo Santos'})

