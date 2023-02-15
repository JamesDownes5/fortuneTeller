# Fortune Teller

Fortune Teller was my EPQ project in college. I was still unsure whether I was going to take computer science at university and decided for my EPQ that I would learn Python and create something, in order to dip my toes into the world of computer science.

The head of computer science at my college that astrology might not be a great hit with computer science professors, so if you could focus on the technical aspects rather than the context there used in that would be great.

I learnt Python through Al Sweigart's book, Automate the Boring Stuff with Python, which I highly recommend everyone, from those want to be more copmuter savvy all the way to those thinking about pursuing a career in computer science.

After frantically searching for ideas for a project, I came across Martyr2-Mega-Project-Ideas-List, one of the ideas to make "a program that checks your horoscope on various astrology sites and puts them together for you each day." I boarden this to be a website that asked for the user's birthday, determine their star sign, list information about their star sign and webscrape their daily horoscope.

## fortuneTeller.py
 
First I made a python program which asked for the user's birthday and return their star sign along with various facts, using tkinter for the GUI.

### Functionality

1. Takes user's birthday input.
2. Returns user's star sign and star sign facts.

### How To Run

1. Have python3 and tkinter installed.
2. Just execute like a regular .py file.

### Skills Learnt

1. Python
2. tkinter

## Django Website

Second I turned the python program into a Djano website, with the addition of webscraping the user's daily horoscope. I hosted this on AWS and assigned a domain to the server. The website which I webscraped the horoscopes from has changed the formatting so unfortunately this feature does not work anymore.

### Functionality

1. Takes user's birthday input.
2. Gives the user the option to view info about their star sign or their daily horoscope.

### How To Run

1. Create a python virtual evironment: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
2. Activate virtual environment: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment
3. Pip install required packages: python3 -m pip install -r requirements.txt
4. Start Django Server: python3 myWebsite/manage.py runserver
5. Go to localhost:8000 on your web browser.

### Skills Learnt

1. Django
2. Webscraping with beautifulsoup4
3. Hosting a website on AWS
4. Adding a domain to a DNS server