from django.shortcuts import render, redirect
from . import util
from django import forms
from django.contrib import messages
from django.urls import reverse 
from django.http import HttpResponseRedirect
import random

class createNewEntry(forms.Form):
    title = forms.CharField(widget=forms.Textarea, label="Title")
    content = forms.CharField(widget=forms.Textarea, label="Content")

class editEntry(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label="Content")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if title in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
             "title": title,
             "content": util.get_entry(title)
            })
    else:
        return render(request, "encyclopedia/notFound.html")

def search(request):
    search_string = request.GET.get('q')

    if search_string in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
            "search": util.get_entry(search_string)
        })
    else:
        return render(request, "encyclopedia/searchResults.html", {
            "entries": util.list_entries(),
            "search": search_string
        })
    
def createEntry(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html", {
            "form": createNewEntry()
        })
    
    elif request.method == "POST":
        form = createNewEntry(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

        if title in util.list_entries():
            messages.error(request, 'This page title already exists! Please go to that title page and edit it instead!')
            return render(request, "encyclopedia/create.html", {
                "form": form
            })
        else:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('entry', args=[title]))
    
def edit(request, title):
    if request.method == "GET":
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "form": editEntry(initial={'content': util.get_entry(title)})
        })
    
    elif request.method == "POST":
        form = editEntry(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('entry', args=[title]))
def randomGenerator(request):
    randomNum = random.randrange(0, len(util.list_entries()))
    title = util.list_entries()[randomNum]

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": util.get_entry(title)
    })