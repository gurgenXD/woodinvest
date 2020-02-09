from feedback.forms import CallBackForm
from core.models import Index
from contacts.models import Social


def context_info(request):
    callback_form = CallBackForm()
    socials = Social.objects.all()

    index = Index.objects.first()

    main_phone = index.phone
    main_address = index.address

    context = {
        'callback_form': callback_form,
        'socials': socials,
        'main_phone': main_phone,
        'main_address': main_address,
    }

    return context