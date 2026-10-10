from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.
def home(request):
    q = request.GET.get('q', '')
    products = Product.objects.all().order_by('-created_at')
    if q:
        products = products.filter(name__icontains=q)
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'products': products, 'categories': categories, 'q': q})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/Product_detail.html',{'product': product})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category_detail.html', {'category': category, 'products': products})