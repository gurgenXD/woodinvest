from django.shortcuts import render, get_object_or_404
from django.views import View
from products.models import Product
from django.db.models import Q
from feedback.forms import FeedBackForm


class ProductsView(View):
    def get(self, request):
        products = Product.objects.filter(is_active=True)

        context = {
            'products': products,
        }

        return render(request, 'products/products.html', context)


class ProductView(View):
    def get(self, request, product_slug):
        product = get_object_or_404(Product, slug=product_slug, is_active=True)

        s_products = Product.objects.filter(is_active=True).exclude(id=product.id)
        similar_products = s_products.filter(Q(category__icontains=product.category)|
                                                   Q(title__icontains=product.title)).distinct()[:4]
        if not similar_products:
            similar_products = s_products[:4]

        feedback_form = FeedBackForm()

        images = product.images.all()

        slider_elems = [(nmb, val) for nmb, val in enumerate(images)]

        context = {
            'product': product,
            'similar_products': similar_products,
            'feedback_form': feedback_form,
            'slider_elems': slider_elems,
        }

        return render(request, 'products/product.html', context)
