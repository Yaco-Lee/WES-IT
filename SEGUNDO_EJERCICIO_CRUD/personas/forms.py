from django import forms


class PersonaForm(forms.Form):
        nombre = forms.CharField()
        apellido = forms.CharField()
        dni = forms.IntegerField(min_value=0)
        fecha_nac = forms.CharField(widget=forms.TextInput(attrs={"class": "datepicker"}))

