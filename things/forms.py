from django import forms

"""Forms of the project."""


class  ThingForm(forms.Form):
    name = forms.CharField(label='Name', max_length=35)
    description= forms.CharField(widget=forms.Textarea)
    quantity=forms.CharField(widget=forms.NumberInput(attrs={ 'min': 0.0, 'max': 50.0}))
