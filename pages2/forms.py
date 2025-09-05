from django import forms
class LoginForm(forms.Form):
    name = forms.CharField(max_length=150, label="user", required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="password",required=True)