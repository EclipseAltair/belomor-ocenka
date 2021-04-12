# -*- coding: utf-8 -*-
from django.db import models


class Client(models.Model):
    name = models.CharField('Имя', max_length=32, blank=False)
    phone = models.CharField('Телефон', max_length=16, blank=False)
    created_at = models.DateTimeField('Дата заявки', auto_now_add=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'клиента'
        verbose_name_plural = 'Клиенты'
