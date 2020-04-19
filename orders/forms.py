from django import forms
from orders.models import Order

class orderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = [

            'firts_name',
            'last_name',
            'document',
            'address',
            'phone_number',
            'order',
            'description',
            'picture',
        ]

        labels = {

            'firts_name':'Nombre',
            'last_name':'Apellido',
            'document':'D.N.I.',
            'address':'Dirección',
            'phone_number':'Tel.',
            'order':'Solicitud',
            'description':'Describir solicitud',
            'picture':'Adjuntar imagen',
        }

        CHOISES = (
            ('Modulos alimentarios', 'Modulos alimentarios'),
            ('Subsidio','Subsidio'),
            ('Pasajes','Pasajes'),
            ('Material de construcción','Material de construcción'),
            ('Kit sanitario','Kit sanitario'),
            ('Ropero','Ropero'),
            ('Farmacia','Farmacia'),
        )

        widgets = {

            'firts_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'document':forms.TextInput(attrs={'class': 'form-control'}),
            'address':forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control'}),
            'order':forms.Select(choices=CHOISES,attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control','rows':3}),
            'picture':forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

class deliverForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = [
            'state',
            'observation',
            'detail',
            'date_deliver',
            'place',
        ]

        labels = {
            'state':'Aprobar',
            'observation':'Observación',
            'detail':'Tipo',
            'date_deliver':'Fecha',
            'place':'Lugar',
        }

        CHOISES2 = (
            ('Entrevista', 'Entrevista'),
            ('Visita','Visita'),
            ('Entrega','Entrega'),
        )
        widgets = {
            'state':forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'observation':forms.Textarea(attrs={'class': 'form-control','rows':3}),
            'detail':forms.Select(choices=CHOISES2,attrs={'class': 'form-control'}),
            'date_deliver':forms.DateInput(attrs={'class': 'form-control'}),
            'place':forms.TextInput(attrs={'class': 'form-control'}),
        }