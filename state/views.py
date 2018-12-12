from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import State
from car.models import Car

def listcar(request):
    listcar = State.objects.order_by('created_date')
    return render(request, 'state/listcar.html', {'listcar': listcar})

@login_required
def updatecar(request, pk):
    car = get_object_or_404(Car, pk=pk)
    listcar = Car.objects.order_by('created_date')
    return render(request, 'state/updatecar.html',{'car':car, 'listcar':listcar})