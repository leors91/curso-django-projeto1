from django.urls import path
from recipes.views import home, contato, sobre

# HTTP REQUEST <- HTTP RESPONDE

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]
