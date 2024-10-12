from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import fields




class Cars(models.Model):
    INCOME_STATUS = (
        ("mehanika", "mexanika"),
        ("auto gearbox", "avtomat karobka"),
    )
    
    cars_name = models.CharField(max_length=255, verbose_name="Mashina nomi")
    seats = models.IntegerField(default=0)
    choice = models.CharField(max_length=100, choices=INCOME_STATUS, verbose_name="Ishlash usuli")
    price_days = models.IntegerField(default=0, verbose_name="kunlik to'lov")
    picture = models.ImageField(upload_to="img", null=True, blank=True)

    
    def str(self):
        return self.cars_name
    
    class Meta:
        verbose_name = "Mashina ro'yxati"
        verbose_name_plural = "Mashinalar ro'yxati"
    
class Car(models.Model):
    name = models.ForeignKey(Cars, on_delete=models.CASCADE, verbose_name="Mashina nomi")
    car_owner = models.CharField(max_length=255, verbose_name="Mashina oluvchi shaxs")
    bags = models.IntegerField(default=0)
    picture = models.ImageField(upload_to="img", blank=True, null=True)

    def str(self):
        return self.name
    
    class Meta:
        verbose_name = 'Mashina'
        verbose_name_plural = 'Mashinalar'


class CarAdvantages(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    fuel_consumption = models.CharField(max_length = 150)
    electric_combined = models.IntegerField()
    touchscreen_display = models.IntegerField()
    light = models.CharField(max_length=50)
    forward_collision = models.CharField(max_length=222)
    fire = models.CharField(max_length=121)
    stop_and_go = models.CharField(max_length=222)
    b_c_w = models.CharField(max_length=222)


    class Meta:

        verbose_name =  "Mashina afzalligi"
        verbose_name_plural =  "Mashina afzalliklari"

    def str(self):
        pass


class Car_description(models.Model):
    des = models.ForeignKey(Car, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Izoh")
    
    class Meta:
        verbose_name = "Mashina ha1qida ma'lumot"
        verbose_name_plural = "Mashina ha1qida ma'lumotlar"    


class Include(models.Model):
    include = models.ForeignKey(Car, on_delete=models.CASCADE)
    sentence1 = models.CharField(max_length=500, null=True)
    sentence2 = models.CharField(max_length=500, null=True)
    sentence3 = models.CharField(max_length=500, null=True)
    sentence4 = models.CharField(max_length=500, null=True)
    sentence5 = models.CharField(max_length=500, null=True)
    sentence6 = models.CharField(max_length=500, null=True)
    
    
class CoolModelBro(models.Model):
    limited_integer_field = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )


class CarOwner(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Ismi")
    places = models.SmallIntegerField()
    description = models.TextField(verbose_name="Izoh")
    joined = models.CharField(max_length=255)
    response = models.ForeignKey(CoolModelBro, on_delete=models.CASCADE)
    response_time = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Mashina oluvshi shaxs'
        verbose_name_plural = 'Mashina oluvshi shaxslar'
        
        
class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Nomi")
    description = models.TextField(verbose_name="Izoh")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    
    class Meta:
        verbose_name = "komment"
        verbose_name_plural  = "kommentlar"
    
    
class CarInformation(models.Model):
    title  = models.CharField(max_length=222, verbose_name="Sarlavha")
    cancellation_policy_title = models.CharField(max_length=121, verbose_name="Bekor qilish ko'rsatmasi")
    cancellation_policy_description = models.TextField(verbose_name="Bekor qilish ko'rsatmasi izohi")
    special_note_title = models.CharField(max_length=100, verbose_name="Maxsus qayd")
    special_note_description = models.TextField(verbose_name="Maxsus qayd izohi")
    
    
    class Meta:
        verbose_name = "Bilish kerak bo'lgan narsalar"

    def str(self):
        return self.title
    
    
    
class CarCost(models.Model):
    title = models.ForeignKey(Car, on_delete=models.CASCADE)
    # hotel = models.ForeignKey(HotelInCity, on_delete=models.CASCntegerField(null=True)
    day = models.IntegerField(default=0)
    car_pick_up = models.DateField()
    car_drop_off = models.DateField()
    car_price_per_day = models.IntegerField(default=0, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    discount = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(99),
            MinValueValidator(0)
        ]
    )
    
    