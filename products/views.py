from django.shortcuts import render, get_object_or_404
from django.views import View
from products.models import Product


class ProductsView(View):
    def get(self):
        products = Product.objects.filter(is_active=True)

        context = {
            'products': products,
        }

        return render(self.request, 'products/products.html', context)


class ProductView(View):
    def get(self, product_slug):
        product = get_object_or_404(Product, slug=product_slug, is_active=True)

        context = {
            'product': product,
        }

        return render(self.request, 'products/product.html', context)
