from django import forms


class SignInForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={'placeholder': 'e.g. user@example.com'}),
        required=True
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': '*******'}),
        required=True
    )


class SignUpForm(forms.Form):
    first_name = forms.CharField(label="First name", required=True, widget=forms.TextInput(attrs={'placeholder': 'e.g. Joe'}))
    last_name = forms.CharField(label="Last name", required=True, widget=forms.TextInput(attrs={'placeholder': 'e.g. Doe'}))
    phone = forms.CharField(label='Phone', required=True, widget=forms.TextInput(attrs={'placeholder': 'e.g. +1 00 987 4561'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'placeholder': 'e.g. joe.doe@example.com'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': '*******'}), required=True)
    password_again = forms.CharField(label='Password again', widget=forms.PasswordInput(attrs={'placeholder': '*******'}), required=True)
