from django.db import models
from django.utils import timezone
 
class State(models.Model):
    number = models.CharField(max_length=15) 
    username = models.CharField(max_length=150)
    departure_date = models.DateTimeField(blank=True, null=True)
    arrival_date = models.DateTimeField(blank=True, null=True)
    departure_place_name = models.CharField(max_length=15, blank=True, null=True)
    arrival_place_name = models.CharField(max_length=15, blank=True, null=True)
    departure_coord = models.CharField(max_length=15, blank=True, null=True)
    arrival_coord = models.CharField(max_length=15, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    car_state = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def create(self):
        self.created_date = timezone.now()
        self.save() 

    def __str(self):
        return self.number
