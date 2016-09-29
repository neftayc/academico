from django.shortcuts import render
from .models import Evento, Category
# Create your views here.
def index(request):
    eventos = Evento.objects.all().order_by('-creado')[:6]
    categorias = Category.objects.all()
    return render(request, 'notas/index.html', {'eventos': eventos, 'categorias': categorias})
