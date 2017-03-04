from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Notebook

def index(request):
        # handle form submission
        if request.method = 'POST':
            title = request.POST.get('title')
            notes = requeset.POST.get('notes')
        # prepare the notes before saving to database
        notebook = Notebook(title=title, notes=notes)
        notebook.save()
        # redirect to homepage after saving
        return redirect('/')
    # all get requests will be handled here
    notes = Notebook.objects()
    return render(request,"index.html",{"context":notes},)

