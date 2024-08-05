from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm

import locale

from .models import User, Listing

class CreateListing(ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "startingBid", "image", "category"]

def index(request):
    return render(request, "auctions/index.html", {
        "active_listings": Listing.objects.all(),
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    if request.method == "GET":
        return render(request, "auctions/create_listing.html", {
            "form": CreateListing()
        })
    else:
        form = CreateListing(request.POST, request.FILES)
        if form.is_valid():

            # Attempt to create new listing
            new_listing = form.save()   

            return HttpResponseRedirect(reverse('listing', args=[new_listing.title]))

    
def listing(request, title):

    listing = Listing.objects.get(title__iexact=title)
    listingInWatchlist = request.user in listing.watchlist.all()

    print(listingInWatchlist)
    locale.setlocale(locale.LC_ALL, '')

    return render(request, "auctions/listing.html", {
        "title": listing.title,
        "description": listing.description,
        "startingBid": listing.formattedBid(),
        "image": listing.image,
        "category": listing.category,
        "isInWatchlist": listingInWatchlist
    })

def edit_watchlist(request, action, id):
    listing = Listing.objects.get(title__iexact=id)
    user = request.user
    if action == 'add':
        listing.watchlist.add(user)
        return HttpResponseRedirect(reverse('watchlist'))
    else:
        listing.watchlist.remove(user)
        return HttpResponseRedirect(reverse('watchlist'))

def watchlist(request):
    user = request.user
    listings = user.listingWatchlist.all()

    return render(request, "auctions/watchlist.html", {
        "watchlist": listings,
        "listLength": len(listings)
    })

def categories(request):
    return render(request, "auctions/categories.html", {
        "categories": Listing.categories
    })

def category(request, category):
    listings = Listing.objects.filter(category=category)
    return render(request, "auctions/category.html", {
        "listings": listings,
        "listings_len": len(listings)
    })