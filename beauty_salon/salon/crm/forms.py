from django import forms


class SiteForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Имя'}))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'class': 'contactus', 'placeholder': 'Email'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Телефон'}))
    message = forms.CharField(max_length=250, widget=forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Сообщение'}))



