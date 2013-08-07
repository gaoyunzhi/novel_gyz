from django import forms

class NovelRequestForm(forms.Form):
    url = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=254)
    name = forms.CharField(max_length=40, required=False)
    author = forms.CharField(max_length=40, required=False)
    filename = forms.CharField(max_length=200, required=False)

    
