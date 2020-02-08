from django.shortcuts import render
from django.views import View
from contacts.models import *
# from callback.forms import CallBackForm


class ContactsView(View):
    def get(self):
        addresses = Address.objects.all()
        phones = Phone.objects.all()
        emails = Email.objects.all()
        map_code = MapCode.objects.first()
        socials = Social.objects.first()

        # callback_form = CallBackForm()

        context = {
            'addresses': addresses,
            'phones': phones,
            'emails': emails,
            'map_code': map_code,
            'socials': socials,
            # 'callback_form': callback_form,
        }
        return render(self.request, 'contacts/contacts.html', context)
