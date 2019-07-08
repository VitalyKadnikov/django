from django.shortcuts import render

def main(request):
    return render(request, 'mainapp/main.html', context={'username':'Ivan'})

def products(request):
    return render(request, 'mainapp/products.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')