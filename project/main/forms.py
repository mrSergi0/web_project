from django import forms
from .models import Post, Request


class AddPost(forms.Form):
    
    title = forms.CharField(max_length=200, label="Тема")
    content = forms.CharField(widget=forms.Textarea, label="Отзыв")
    image = forms.ImageField()
    

class AddRequest(forms.Form):
    name = forms.CharField(max_length=200, label="Имя")
    email = forms.EmailField(label="Email")
    phone_number = forms.CharField(max_length=12, label="Телефон")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")