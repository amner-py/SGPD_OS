from django import forms

class RespuestaFiltroForm(forms.Form):
    respondido__after = forms.DateField(label='Fecha inicio',widget=forms.SelectDateWidget(attrs={
        'class':'form-control',
        'type':'date'
    }))
    respondido__before = forms.DateField(label='Fecha fin',widget=forms.SelectDateWidget(attrs={
        'class':'form-control',
        'type':'date'
    }))
