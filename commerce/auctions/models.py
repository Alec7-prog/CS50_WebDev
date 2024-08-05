from django.contrib.auth.models import AbstractUser
from django.db import models    

class User(AbstractUser):
    pass 

class Listing(models.Model):
    categories = {
        "Fashion": "Fashion",
        "Toys": "Toys",
        "Electronics": "Electronics", 
        "Home": "Home"
    }

    default_val = 0.01
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    startingBid = models.FloatField(default=default_val)
    image = models.ImageField(upload_to="auctions/static/auctions/images/", null=True, blank=True)
    category = models.CharField(max_length=64, choices=categories, null=True, blank=True)   
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="listingWatchlist")
    
    def __str__(self):
        return self.title