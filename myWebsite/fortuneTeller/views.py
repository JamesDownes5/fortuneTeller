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

    return render(request, 'fortuneteller/home.html', {'form': form})

def menu(request):
    if request.method == 'POST':
        form = OptionForm(request.POST)
        
        if form.is_valid():
            val = form.cleaned_data.get("btn")
            
            if val == 'Info':
                return HttpResponseRedirect('/fortuneteller/info/', {'starSign' : starSign })
            
            elif val == 'Daily Horoscope':
                return HttpResponseRedirect('/fortuneteller/dailyhoroscope/', {'starSign' : starSign })
            
    else:
        form = OptionForm()

    return render(request, 'fortuneteller/menu.html', {'starSign' : personalStarSign, 'form' : form})

def info(request):

    if personalStarSign == 'Aquarius':                                          #TODO Maybe use a for loop with a list of star signs to cycle through
        return render(request, 'fortuneteller/starSignInfo/aquarius.html')

    elif personalStarSign == 'Aries':
        return render(request, 'fortuneteller/starSignInfo/aries.html')

    elif personalStarSign == 'Cancer':
        return render(request, 'fortuneteller/starSignInfo/cancer.html')

    elif personalStarSign == 'Capricorn':
        return render(request, 'fortuneteller/starSignInfo/capricorn.html')

    elif personalStarSign == 'Gemini':
        return render(request, 'fortuneteller/starSignInfo/gemini.html')

    elif personalStarSign == 'Leo':
        return render(request, 'fortuneteller/starSignInfo/leo.html')

    elif personalStarSign == 'Libra':
        return render(request, 'fortuneteller/starSignInfo/libra.html')

    elif personalStarSign == 'Pisces':
        return render(request, 'fortuneteller/starSignInfo/pisces.html')

    elif personalStarSign == 'Sagittarius':
        return render(request, 'fortuneteller/starSignInfo/sagittarius.html')

    elif personalStarSign == 'Scorpio':
        return render(request, 'fortuneteller/starSignInfo/scorpio.html')

    elif personalStarSign == 'Taurus':
        return render(request, 'fortuneteller/starSignInfo/taurus.html')

    elif personalStarSign == 'Virgo':
        return render(request, 'fortuneteller/starSignInfo/virgo.html')


def DailyHoroscope(request):

    dailyHoroscope, dailyLove, dailyWork, dailyDating, dailyBonus = DailyHoroscopeWebscraper(personalStarSign)

    return render(request, 'fortuneteller/dailyhoroscope.html', {'starSign' : personalStarSign, 'dailyHoroscope' : dailyHoroscope, 'dailyLove' : dailyLove, 'dailyWork' : dailyWork, 'dailyDating' : dailyDating, 'dailyBonus' : dailyBonus })