from django.shortcuts import render
from car.models import Car
from django.shortcuts import render, redirect, get_object_or_404


def listcar(request):
    listcar = Car.objects.order_by('created_date')
    return render(request, 'state/listcar.html', {'listcar': listcar})

def updatecar(request, pk):
    car = get_object_or_404(Car, pk=pk)
    listcar = Car.objects.order_by('created_date')
    return render(request, 'state/updatecar.html',{'car':car, 'listcar':listcar})