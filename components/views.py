from django.shortcuts import render

def components (request):
    return render (request, 'components/components.html')