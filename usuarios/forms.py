from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label ="Nome de Login", 
        required = True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nome de Login"
            }
        )
    )
    senha = forms.CharField(
        label ="Senha", 
        required = True, 
        max_length=70, 
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome = forms.CharField(
        label ="Nome de Cadastro", 
        required = True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nome"
            }
        )
    )
    email = forms.EmailField(
        label ="Email", 
        required = True, 
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email"
            }
        )
    )
    senha = forms.CharField(
        label ="Senha", 
        required = True, 
        max_length=70, 
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Senha"
            }
        )
    )
    senha2 = forms.CharField(
        label ="Confirmação de Senha", 
        required = True, 
        max_length=70, 
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirmação de Senha"
            }
        )
    )