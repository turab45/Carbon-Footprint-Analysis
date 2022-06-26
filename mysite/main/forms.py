from django import forms

class CreateNewList(forms.Form):
    title = forms.CharField(label="Name", max_length=50)