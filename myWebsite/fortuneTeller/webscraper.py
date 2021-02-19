from bs4 import BeautifulSoup
import requests

def DailyHoroscopeWebscraper(starSign):
    source = requests.get('https://www.astrology.com/horoscope/daily/' + starSign + '.html').text

    soup = BeautifulSoup(source, 'lxml')

    main = soup.find('main')

    dailyHoroscope = main.find('div', id='content').p.text
    dailyLove = main.find('div', id='content-love').p.text
    dailyWork = main.find('div', id='content-work').p.text
    dailyDating = main.find('div', id='content-dating').text.strip()
    dailyBonus = main.find('div', id='content-bonus').text.strip()

    return (dailyHoroscope, dailyLove, dailyWork, dailyDating, dailyBonus)
