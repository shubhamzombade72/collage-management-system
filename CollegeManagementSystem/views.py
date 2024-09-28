
from django.shortcuts import render


def indexpage(request):
    return render(request, 'Template/index.html')  