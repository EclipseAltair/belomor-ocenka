# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import ClientForm


def home(request):
    form = ClientForm(request.POST or None)
    return render(request, 'main/index.html', locals())


def feedback(request):
    if request.POST:
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            name = request.POST['name']
            phone = request.POST['phone']
            # subject = 'Новый клиент!'
            # message = 'Имя: ' + name + ' | Номер телефона: ' + phone
            # sender = 'digitalrushmailer@gmail.com'
            # recipient = 'belomorocenka@yandex.ru'
            # send_mail(subject, message, sender, [recipient], fail_silently=False)
            return JsonResponse({})


def error_404(request, exception=None):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)
