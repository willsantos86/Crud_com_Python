from django.shortcuts import render, redirect
from app.forms import DadosForm
from app.models import Dados


# Create your views here.
def index(request):
    data = {}
    data['db'] = Dados.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = DadosForm
    return render(request, 'form.html', data)

def create(request):
    form = DadosForm(request.POST or None) #Recebe os dados de form.html
    if form.is_valid(): #Verifica se os dados são válidos
        form.save()  #Salva os dados.
        return redirect('index')


def view(request, pk):
    data = {}
    data['db'] = Dados.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Dados.objects.get(pk=pk)
    data['form'] = DadosForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Dados.objects.get(pk=pk)
    form = DadosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('index')



