from django.db import models
from django.db.models import IntegerField, Model
from django.contrib.auth.models import User



class Cars(models.Model):
    INCOME_STATUS = (
        ("mehanika", "mehanika"),
        ("auto gearbox", "avtomat karobka"),

    )
    
    cars_name = models.CharField(max_length=255)
    seats = models.IntegerField(default=0)
    choice = models.CharField(max_length=100, choices=INCOME_STATUS, verbose_name="Ishlash usuli")
    price_days = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.cars_name
    
class Car(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    name = models.ForeignKey(Cars, to_field='cars_name', verbose_name=_("Mashina nomi"), on_delete=models.CASCADE)
    car_owner = models.CharField(max_length=255)
    seats = models.IntegerField(default=0)
    bags = models.IntegerField(default=0)
    choice = models.ForeignKey(Cars,to_field= "choice", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Mashina'
        verbose_name_plural = 'Mashinalar'


class Car_Information(models.Model):
    '''Model definition for Car_Information.'''
    fuel_consumption = models.CharField(max_length = 150)
    electric_combined = models.IntegerField()
    touchscreen_display = models.IntegerField()
    light = models.CharField(max_length=50)
    
       


    class Meta:
        '''Meta definition for Car_Information.'''

        verbose_name =  'Car_Information'
        verbose_name_plural =  'Car_Informations'

    def __str__(self):
        pass




















