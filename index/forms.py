from django import forms


class SignInForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)


class SignUpForm(forms.Form):
    first_name = forms.CharField(label="First name", required=True)
    last_name = forms.CharField(label="Last name", required=True)
    phone = forms.CharField(label='Phone', required=True)
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password_again = forms.CharField(label='Password again', widget=forms.PasswordInput, required=True)
