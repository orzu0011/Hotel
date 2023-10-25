from country.models import *


def add_income_items(id):
    objs = HotelInCityCost.objects.filter(hotel=id)
    sum_hotel = 0
    for i in objs:
        sum_hotel += i.total
    return sum_hotel