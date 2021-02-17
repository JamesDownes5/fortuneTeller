from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BirthdayForm, OptionForm
from .logic import *

def home(request):
    if request.method == 'POST':
        form = BirthdayForm(request.POST)
        if form.is_valid():
            
            global personalStarSign
            personalStarSign = Finder(form.cleaned_data['usersBirthday'])

            return HttpResponseRedirect('menu/')

    else:
        form = BirthdayForm()

    return render(request, 'fortuneTeller/home.html', {'form': form})

def menu(request):

    if request.method == 'POST':
        form = OptionForm(request.POST)
        if form.is_valid():
            val = form.cleaned_data.get("btn")
    else:
        form = OptionForm()

    return render(request, 'fortuneTeller/menu.html', {'starSign' : personalStarSign, 'form' : form})

def sagittarius(request):
    return render(request, 'fortuneTeller/starSignInfo/sagittarius.html')