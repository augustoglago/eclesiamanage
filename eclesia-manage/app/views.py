from django.shortcuts import render
from . models import *

def consulta1(request):
    consultaMembro = Membro.objects.all()
    context = {'consultaMembro': consultaMembro}
    return render(request, 'consulta/consultaMembro.html', context)

def consulta2(request):
    consultaMinisterio = Ministerio.objects.all()
    context = {'consultaMinisterio': consultaMinisterio}
    return render(request, 'consulta/consultaMinisterio.html', context)

def consulta3(request):
    consultaVisita = Visita.objects.all()
    context = {'consultaVisita': consultaVisita}
    return render(request, 'consulta/consultaVisita.html', context)

def consulta4(request):
    consultaTipoInstrumento = TipoInstrumento.objects.all()
    context = {'consultaTipoInstrumento': consultaTipoInstrumento}
    return render(request, 'consulta/consultaTipoInstrumento.html', context)

def consulta5(request):
    consultaFuncao = Funcao.objects.all()
    context = {'consultaFuncao': consultaFuncao}
    return render(request, 'consulta/consultaFuncao.html', context)

def consulta6(request):
    consultaInstrumento = Instrumento.objects.all()
    context = {'consultaInstrumento': consultaInstrumento}
    return render(request, 'consulta/consultaInstrumento.html', context)

def consulta7(request):
    consultaPequenoGrupo = PequenoGrupo.objects.all()
    context = {'consultaPequenoGrupo': consultaPequenoGrupo}
    return render(request, 'consulta/consultaPequenoGrupo.html', context)

def consulta8(request):
    consultaEvento = Evento.objects.all()
    context = {'consultaEvento': consultaEvento}
    return render(request, 'consulta/consultaEvento.html', context)