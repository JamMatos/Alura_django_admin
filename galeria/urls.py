from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem', imagem, name='imagem'),
    #path('imagem.html/index.html', index),
    #path('imagem.html/imagem.html', imagem)
]