from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        content = f'Nome: {name} \nEmail: {email} \nAssunto: {subject} \nMensagem: {message}'

        mail = EmailMessage(
            subject=subject,
            body=content,
            from_email='contato@vitor.com.br',
            to=['contato@vitor.com.br'],
            headers={'Reply-To': email},
            reply_to=[email]    
        )
        mail.send()