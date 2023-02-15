from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BirthdayForm, OptionForm
from .logic import *
from .webscraper import *

def home(request):
    if request.method == 'POST':
        form = BirthdayForm(request.POST)
        if form.is_valid():
            
            global personalStarSign
            personalStarSign = Finder(form.cleaned_data['usersBirthday'])

            return HttpResponseRedirect('menu/', {'starSign' : personalStarSign})

    else:
        form = BirthdayForm()

    return render(request, 'fortuneTeller/home.html', {'form': form, 'title' : 'Home'})

def menu(request):
    if request.method == 'POST':
        form = OptionForm(request.POST)
        
        if form.is_valid():
            val = form.cleaned_data.get("btn")
            
            if val == 'Info':
                return HttpResponseRedirect('/info/', {'starSign' : starSign })
            
            elif val == 'Daily Horoscope':
                return HttpResponseRedirect('/dailyhoroscope/', {'starSign' : starSign })
            
    else:
        form = OptionForm()

    return render(request, 'fortuneTeller/menu.html', {'starSign' : personalStarSign, 'form' : form, 'title' : 'Menu'})

def info(request):

    if personalStarSign == 'Aquarius':                                          #TODO Maybe use a for loop with a list of star signs to cycle through
        return render(request, 'fortuneTeller/starSignInfo/aquarius.html', {'title' : 'Info'})

    elif personalStarSign == 'Aries':
        return render(request, 'fortuneTeller/starSignInfo/aries.html', {'title' : 'Info'})

    elif personalStarSign == 'Cancer':
        return render(request, 'fortuneTeller/starSignInfo/cancer.html', {'title' : 'Info'})

    elif personalStarSign == 'Capricorn':
        return render(request, 'fortuneTeller/starSignInfo/capricorn.html', {'title' : 'Info'})

    elif personalStarSign == 'Gemini':
        return render(request, 'fortuneTeller/starSignInfo/gemini.html', {'title' : 'Info'})

    elif personalStarSign == 'Leo':
        return render(request, 'fortuneTeller/starSignInfo/leo.html', {'title' : 'Info'})

    elif personalStarSign == 'Libra':
        return render(request, 'fortuneTeller/starSignInfo/libra.html', {'title' : 'Info'})

    elif personalStarSign == 'Pisces':
        return render(request, 'fortuneTeller/starSignInfo/pisces.html', {'title' : 'Info'})

    elif personalStarSign == 'Sagittarius':
        return render(request, 'fortuneTeller/starSignInfo/sagittarius.html', {'title' : 'Info'})

    elif personalStarSign == 'Scorpio':
        return render(request, 'fortuneTeller/starSignInfo/scorpio.html', {'title' : 'Info'})

    elif personalStarSign == 'Taurus':
        return render(request, 'fortuneTeller/starSignInfo/taurus.html', {'title' : 'Info'})

    elif personalStarSign == 'Virgo':
        return render(request, 'fortuneTeller/starSignInfo/virgo.html', {'title' : 'Info'})


def DailyHoroscope(request):

    dailyHoroscope, dailyLove, dailyWork, dailyDating, dailyBonus = DailyHoroscopeWebscraper(personalStarSign)

    return render(request, 'fortuneteller/dailyhoroscope.html', {'starSign' : personalStarSign, 'dailyHoroscope' : dailyHoroscope, 'dailyLove' : dailyLove, 'dailyWork' : dailyWork, 'dailyDating' : dailyDating, 'dailyBonus' : dailyBonus, 'title' : 'Daily Horoscope'})