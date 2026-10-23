from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request):
    products = Product.objects.select_related("category")
    q = request.GET.get("q", "").strip()
    if q:
        products = products.filter(name__icontains=q)
    return render(request, "shop/home.html", {
        "products": products,
        "categories": Category.objects.all(),
        "q": q,
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, "shop/home.html", {
        "products": category.products.all(),
        "categories": Category.objects.all(),
        "current": category,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product.objects.select_related("category"), slug=slug)
    related = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:4]
    return render(request, "shop/product_detail.html", {"product": product, "related": related})