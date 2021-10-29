from django.shortcuts import render, redirect
from app.forms import IngressosForm
from app.models import Ingressos
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    data = {}
    pag = Ingressos.objects.all()
    paginator = Paginator(pag, 3)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

    # SEM PAGINAÇÃO
    # data['db'] = Ingressos.objects.all()
    # return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = IngressosForm()
    return render(request, 'form.html', data)


def create(request):
    form = IngressosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Ingressos.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Ingressos.objects.get(pk=pk)
    data['form'] = IngressosForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Ingressos.objects.get(pk=pk)
    form = IngressosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')


def delete(request, pk):
    db = Ingressos.objects.get(pk=pk)
    db.delete()
    return redirect('home')