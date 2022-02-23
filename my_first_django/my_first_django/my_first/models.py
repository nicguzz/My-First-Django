from django.db import models
from django.forms import CharField

class Order(models.Model):
    MEALS = (
            ('Cheeseburger', 'Cheeseburger'),
            ('Hot dog','Hot dog'),
            ('Pizza','Pizza'),
            ('T-Bone', 'T-Bone'),
            ('French fries', 'French fries'),
            ('Salmon tartar', 'Salmon tartar')
    )

    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    meal = models.TextField(max_length=20, choices=MEALS)
