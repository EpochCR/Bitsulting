from django import forms
from bitsulting.models import Response, Question, Category

class ResponseForm(forms.ModelForm):
    bitcoinAddress = forms.CharField(label="address", widget=forms.TextInput(attrs={'size':'38'}),required=True,)
    text = forms.CharField(label="", widget=forms.Textarea(attrs={'cols': 120, 'rows': 15}), required=True)
    class Meta:
        model = Response
        fields = ('bitcoinAddress', 'text',)