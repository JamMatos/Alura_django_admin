from django import forms

class LoginForms(forms.Form):
    usuario = forms.CharField(
        label= "Nome de Login",
        required=True,
        max_length=100,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    ) 
    senha = forms.CharField(
        label= "Senha",
        required=True,
        max_length=16,
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    usuario = forms.CharField(
        label= "Nome Completo",
        required=True,
        max_length=100,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    ) 
    email = forms.EmailField(
        label= "Email",
        required=True,
        max_length=100,
        widget = forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joaosilva@xpto.com"
            }
        )
        
    )
    senha = forms.CharField(
        label= "Senha",
        required=True,
        max_length=16,
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha2 = forms.CharField(
        label= "Confirmação de senha",
        required=True,
        max_length=16,
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('usuario')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha')
        senha_2 = self.cleaned_data.get('senha2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2
