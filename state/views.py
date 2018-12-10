from django.shortcuts import render
from car.models import Car

def listcar(request):
    listcar = Car.objects.order_by('created_date')
    return render(request, 'state/listcar.html', {'listcar': listcar})