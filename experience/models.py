from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.db.models import fields
    
class Experiences_list(models.Model):
    '''Model definition for Experiences_list.'''
    title = models.CharField(max_length = 150)
    person_cost = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    # picture = models.ImageField(upload_to="img", blank=True, null=True)
    class Meta:
        '''Meta definition for Experiences_list.'''

        verbose_name = 'Experiences_list'
        verbose_name_plural = 'Experiences_lists'

    def str(self):
        return self.title


class Experiences(models.Model):
    '''Model definition for Experiences.'''
    title = models.ForeignKey(Experiences_list, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    hour = models.TimeField(auto_now=False)
    number_of_people = models.SmallIntegerField()
    language = models.CharField(max_length=144)
    picture = models.ImageField(upload_to="img", blank=True, null=True)

    class Meta:
        '''Meta definition for Experiences.'''

        verbose_name = 'Experiences'
        verbose_name_plural = 'Experiencess'

    def str(self):
        return self.author

class Experiences_descriptions(models.Model):
    '''Model definition for Experiences_descriptions.'''
    main = models.ForeignKey(Experiences, on_delete=models.CASCADE)
    title = models.CharField(max_length=144)
    descriptions1 = models.CharField(max_length = 150)
    descriptions2 = models.CharField(max_length = 150, null=False, blank=False)
    descriptions3 = models.CharField(max_length = 150, null=False, blank=False)
    descriptions4 = models.CharField(max_length = 150, null=False, blank=False)

    class Meta:
        '''Meta definition for Experiences_descriptions.'''

        verbose_name = 'Experiences_descriptions'
        verbose_name_plural = 'Experiences_descriptionss'

    def str(self):
        return self.title


class Include(models.Model):
    '''Model definition for Include.'''
    main = models.ForeignKey(Experiences, on_delete=models.CASCADE)
    include = models.CharField(max_length=150)
    
    class Meta:
        '''Meta definition for Include.'''

        verbose_name = 'Include'
        verbose_name_plural = 'Includes'

    def str(self):
        return self.include

class Comment(models.Model):
    post = models.ForeignKey(Experiences, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def str(self):
        return 'Comment {} by {}'.format(self.description, self.name)



class Things_to_know(models.Model):
    '''Model definition for Experiences_descriptions.'''
    main = models.ForeignKey(Experiences, on_delete=models.CASCADE)
    title = models.CharField(max_length=144)
    descriptions1 = models.CharField(max_length = 150, null=True, blank=True)
    descriptions2 = models.CharField(max_length = 150, null=True, blank=True)
    descriptions3 = models.CharField(max_length = 150, null=True, blank=True)
    descriptions4 = models.CharField(max_length = 150, null=True, blank=True)
    class Meta:

        verbose_name = 'know'
        verbose_name_plural = 'knows'
    
    def str(self):
        return self.title
    
class ExperiencesCost(models.Model):
    title = models.ForeignKey(Experiences, on_delete=models.CASCADE)
    # hotel = models.ForeignKey(HotelInCity, on_delete=models.CASCntegerField(null=True)
    person_price_per_day = models.IntegerField(null=True, blank=True)
    person_check_in = models.DateField(default=datetime.now)
    person_check_out = models.DateField(default=datetime.now)
    guests = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    guests_main = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    service_charge = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    total_cost = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    Adults = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    Children = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    Infants = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    
    discount = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(99),
            MinValueValidator(0)
        ]
    )
    
    
    class Meta:
        verbose_name = 'HotelInCityCost'
        verbose_name_plural = 'HotelInCityCosts'

    def str(self):
        return self.room_price_per_day
