from django.shortcuts import render, get_object_or_404
from django.views import View
from services.models import Service


class ServicesView(View):
    def get(self):
        services = Service.objects.filter(is_active=True)

        context = {
            'services': services,
        }
        return render(self.request, 'services/services.html', context)
