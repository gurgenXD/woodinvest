from django import forms
from orders.models import Order
from orders.models import Region


class OrderForm(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label='Регион',
                                    widget=forms.Select(attrs={'class': 'form-control smaller'}))

    class Meta:
        model = Order
        fields = ('service', 'region', 'address', 'material', 'deadline', 'contact', 'phone', 'email', 'note')
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес'}),
            'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Вид сырья и объём'}),
            'deadline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Сроки оказания услуг'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Контактное лицо'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (___) ___-__-__', 'id': 'ServiceModalPhone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Примечание', 'rows': 4}),
        }
