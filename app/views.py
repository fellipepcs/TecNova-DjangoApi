from django.core import paginator
from django.shortcuts import render, redirect
from app.forms import ClientesForm
from app.models import Clientes
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Clientes.objects.filter(nomeCliente__icontains= search)
    else:
        data['db'] = Clientes.objects.all()

    #data['db'] = Clientes.objects.all()
    #all = Clientes.objects.all()
    #paginator = Paginator(all, 2)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    return render(request, 'index.html',data)


def form(request):
    data = {}
    data['form'] = ClientesForm()
    return render(request, 'form.html', data)


def create(request):
    form = ClientesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    data['form'] = ClientesForm(instance=data['db'])
    return  render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    form = ClientesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Clientes.objects.get(pk=pk)
    db.delete()
    return redirect('home')