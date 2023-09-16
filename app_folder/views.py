from django.shortcuts import render

def home(request):
    return render(request, 'apps/home.html', {})

def about(request):
    return render(request, 'apps/about.html', {})

def blog(request):
    return render(request, 'apps/blog.html', {})

def cart(request):
    return render(request, 'apps/cart.html', {})

def checkout(request):
    return render(request, 'apps/checkout.html', {})

def contact(request):
    return render(request, 'apps/contact.html', {})

def product(request):
    return render(request, 'apps/product.html', {})

def product_single(request):
    return render(request, 'apps/product_single.html', {})