from django.db import models
from django.db.models import IntegerField, Model
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


class Country(models.Model):
    city_name = models.CharField(max_length=255)
    properties = models.IntegerField()
    picture = models.ImageField(upload_to="img", blank=True, null=True)

    class Meta:
        verbose_name = "Shahar nomi"
        verbose_name_plural = "Shahar nomlari"

    def __str__(self):
        return self.city_name


class HotelInCity(models.Model):
    city = models.ForeignKey(Country, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    guests = models.IntegerField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    bathrooms = models.IntegerField()
    stay_information = models.TextField()
    
    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return self.title


class CoolModelBro(Model):
    limited_integer_field = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    places = models.SmallIntegerField()
    description = models.TextField()
    joined = models.CharField(max_length=255)
    response = models.ForeignKey(CoolModelBro, on_delete=models.CASCADE)
    response_time = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.full_name


class Comment(models.Model):
    post = models.ForeignKey(HotelInCity, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'Comment {} by {}'.format(self.description, self.name)


class Information(models.Model):
    hotel = models.ForeignKey(HotelInCity, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    check_in_time_start = models.TimeField()
    check_in_time_finish = models.TimeField()
    check_out_time_start = models.TimeField()
    check_out_time_finish = models.TimeField()
    special_note_title = models.CharField(max_length=100)
    special_note_description = models.TextField()

    def __str__(self):
        return self.hotel


class HotelInCityCost(models.Model):
    # hotel = models.ForeignKey(HotelInCity, on_delete=models.CASCADE)
    room_price_per_day = models.IntegerField(null=True)
    room_check_in = models.DateField(default=datetime.now)
    day = models.IntegerField()
    service_charge = models.IntegerField(default=0)
    total_cost = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    
    class Meta:
        verbose_name = 'HotelInCityCost'
        verbose_name_plural = 'HotelInCityCosts'

    def __str__(self):
        return self.room_price_per_day 

    
    
    
"""        
     
class Total(models.Model):


    class Meta:

        verbose_name = 'Total'
        verbose_name_plural = 'Totals'

    def str(self):
        pass
 """