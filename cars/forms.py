from django import forms
from . import models


class CarForm(forms.ModelForm):
    class Meta:
        model = models.Car
        fields = ['brand', 'name', 'description', 'image', 'price', 'quantity']


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'email', 'body']