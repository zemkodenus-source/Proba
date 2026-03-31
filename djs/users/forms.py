from django.template.defaultfilters import title
from .models import coment
from django.forms import ModelForm , TextInput ,Textarea , DateTimeInput

class commentForms(ModelForm):
    class Meta:
        model = coment
        fields = ['title' , 'about' , 'full_text' , 'data']

        widgets = {
            'title' : TextInput(attrs={
                'class' : 'form-control' ,
                'placeholder' : 'Користувач'
            }) ,
            'about':TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Опис'
            }) ,
            'full_text':Textarea(attrs= {
                'class': 'form-control',
                'placeholder': 'Повний коментар'
            }) ,
            'data':DateTimeInput(attrs= {
                'class': 'form-control',
                'type': 'datetime-local'
            })
        }