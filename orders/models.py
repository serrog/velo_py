# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

class Worker(models.Model):
    POSITIONS = (
        (1, 'Manager'),
        (2, 'Designer'),
        (3, 'Clerk'),
        (4, 'Driver'),
        (5, 'Jobber'), # разнорабочий
        (6, 'Miller'), # фрезеровщик
        (7, 'Fitter'), # сборщик
        (8, 'Accountant'), # бухгалтер
        (9, 'Sysop'), # сисадмин
        (10, 'writer'),
    )
    PERIODS = (
        ('D', 'Day'),
        ('M', 'Month'),
        ('R', 'Payment by results'),
    )

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.full_name()

    def is_manager(self):
        return self.position == 1 and self.fired is Null
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)
    position = models.IntegerField(choices=POSITIONS)
    salary_period = models.CharField(max_length=1, choices=PERIODS)
    salary = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    starting = models.DateField()
    fired = models.DateField(null=True, blank=True)

class Order(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)
    started = models.DateField()
    finished = models.DateField(null=True, blank=True)
    scheduled = models.DateField()
    hold = models.ForeignKey(Worker, limit_choices_to={'position': 1}, )# ответственный

class Job(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)
    started = models.DateField()
    finished = models.DateField(null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, )
    worker = models.ForeignKey(Worker, null=True, blank=True)
    fee = models.DecimalField(max_digits=7, decimal_places=2)
