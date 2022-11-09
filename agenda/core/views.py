from django.shortcuts import render
from core.models import Evento


# Create your views here.

def lista_eventos(request):
    #evento = Evento.objects.get(id=1)
    #esponse = {'evento': evento}
    #return render(request, 'agenda.html', response)

    # pegar o usuario que fez a requisição (proximas duas linhas)
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    #evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
