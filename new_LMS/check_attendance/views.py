from django.shortcuts import render

# Create your views here.


from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def client_view(request):
    return render(request, 'client.html')

def manager_view(request):
    return render(request, 'manager.html')
