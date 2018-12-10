from django.shortcuts import render

def listcar(request):
    return render(request, 'state/listcar.html', {})