from django.shortcuts import render


def frontView(request):
    return render(request, 'home/front.html')

# Create your views here.
