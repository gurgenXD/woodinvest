from django.shortcuts import render, get_object_or_404
from django.views import View
from services.models import Service
from orders.forms import OrderForm
from orders.models import Region


class ServicesView(View):
    def get(self, request):
        services = Service.objects.filter(is_active=True)

        order_form = OrderForm()

        context = {
            'services': services,
            'order_form': order_form,
        }

        return render(request, 'services/services.html', context)
