from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from orders.forms import *
from core.models import MailToString
from services.models import Service
from orders.models import Region


class OrderView(View):
    def post(self, request):
        order_form = OrderForm(request.POST)
        status = 0

        if order_form.is_valid() and request.recaptcha_is_valid:
            current_site = get_current_site(request)
            mail_subject = 'Новый заказ на сайте: ' + current_site.domain
            service = Service.objects.get(id=int(request.POST.get('service'))).title
            region = Region.objects.get(id=int(request.POST.get('region'))).title
            message = render_to_string('orders/order_message.html', {
                'domain': current_site.domain,
                'service': service,
                'region': region,
                'address': request.POST.get('address'),
                'material': request.POST.get('material'),
                'deadline': request.POST.get('deadline'),
                'contact': request.POST.get('contact'),
                'phone': request.POST.get('phone'),
                'email': request.POST.get('email'),
                'note': request.POST.get('note'),
            })
            to_email = MailToString.objects.first().email
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            order_form.save()
            status = 1
            
        context = {
            'status': status,
        }

        return JsonResponse(context)
