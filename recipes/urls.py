from django.urls import path
from recipes.views import home

# HTTP REQUEST <- HTTP RESPONDE

urlpatterns = [
    path('', home),
]
