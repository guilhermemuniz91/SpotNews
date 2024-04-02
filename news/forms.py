from django import forms


class CreateCategoriesForm(forms.Form):
    name = forms.CharField(max_length=200)
