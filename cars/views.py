from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib import messages
# Create your views here.

def car_detail(request, car_id):
    car = models.Car.objects.get(id=car_id)

    if request.method == 'POST':
        if 'buy_now' in request.POST:
            if car.quantity > 0:
                car.buy.add(request.user)
                car.quantity -= 1
                car.save()
                messages.success(request, 'Car purchased successfully!')
            else:
                messages.error(request, 'Car is out of stock!')
        elif 'comment' in request.POST:
            comment_form = forms.CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.car = car
                new_comment.save()
                messages.success(request, 'Comment added successfully!')
    comments = models.Comment.objects.filter(car=car)

    comment_form = forms.CommentForm()

    return render(request, 'detail_of_car.html', {'car': car, 'comments': comments, 'comment_form': comment_form})