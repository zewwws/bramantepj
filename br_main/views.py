from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Product


def home(request):
    products = Product.objects.filter(is_published=True)
    return render(request, 'br_main/home.html', {'products': products})


def product_list(request):
    products = Product.objects.filter(is_published=True)
    groups = [
        (key, label, [p for p in products if p.category == key])
        for key, label in Product.CATEGORY_CHOICES
    ]
    return render(request, 'br_main/product_list.html', {'groups': [g for g in groups if g[2]]})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_published=True)
    related = Product.objects.filter(is_published=True).exclude(pk=product.pk)[:3]
    return render(request, 'br_main/product_detail.html', {'product': product, 'related': related})


def about(request):
    return render(request, 'br_main/about.html')


def contact(request):
    initial = {}
    if slug := request.GET.get('produs'):
        initial['product'] = Product.objects.filter(slug=slug, is_published=True).first()
    form = ContactForm(request.POST or None, initial=initial)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Vă mulțumim! Am primit cererea și vă vom contacta în cel mai scurt timp.')
        return redirect('br_main:contact')
    return render(request, 'br_main/contact.html', {'form': form})
