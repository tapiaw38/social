from django import forms
from orders.models import Order

class orderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = [

            'firts_name',
            'last_name',
            'document',
            'cuil',
            'address',
            'phone_number',
            'order',
            'description',
        ]

        labels = {

            'firts_name':'Nombre',
            'last_name':'Apellido',
            'document':'D.N.I.',
            'cuil':'Cuil',
            'address':'Dirección',
            'phone_number':'Tel.',
            'order':'Solicitud',
            'description':'Describir solicitud',
        }

        CHOISES = (
            ('Modulos alimentarios', 'Modulos alimentarios'),
            ('Material de construcción','Material de construcción'),
            ('Kit sanitario','Kit sanitario'),
            ('Ropero','Ropero'),
            ('Farmacia','Farmacia'),
        )

        widgets = {

            'firts_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'document':forms.TextInput(attrs={'class': 'form-control'}),
            'cuil':forms.TextInput(attrs={'class': 'form-control'}),
            'address':forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control'}),
            'order':forms.Select(choices=CHOISES,attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control','rows':3}),
        }

class deliverForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = [
            'state',
            'observation',
            'date_deliver',
            'place',
        ]

        labels = {
            'state':'Aprobar',
            'observation':'Observación',
            'date_deliver':'Fecha de entrega',
            'place':'Lugar de Entrega',
        }

        widgets = {
            'state':forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'observation':forms.Textarea(attrs={'class': 'form-control','rows':3}),
            'date_deliver':forms.DateInput(attrs={'class': 'form-control'}),
            'place':forms.TextInput(attrs={'class': 'form-control'}),
        }