from django.db import models


class Steward(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    kitchens = models.ManyToManyField('Kitchen', through='Assignment')

class Availability(models.Model):
    days = models.TextField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    steward = models.OneToOneField('Steward', on_delete=models.CASCADE)


class Kitchen(models.Model):
    name = models.CharField(max_length=100)
    head_chef = models.CharField(max_length=100)
    trading_hours = models.ForeignKey('TradingHours', on_delete=models.CASCADE)


class TradingHour(models.Model):
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()


class Assignment(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    steward = models.ForeignKey(Steward, on_delete=models.CASCADE)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)


