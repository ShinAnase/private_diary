from django import forms

class inquiryForm(forms.form):
    name = forms.CharField(label='名前', max_length=30)