from django import forms

"""Forms of the project."""


class  ThingForm(forms.Form):
    name = forms.CharField(label='Name')
    description= forms.CharField(widget=forms.Textarea)
    quality=forms.CharField(widget=forms.NumberInput)
