#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Libraries
from tkinter import *
from tkinter import ttk

class homeScreen():                           # Home Screen Frame, which asks for the users age

    starSign = {'january': {range(1, 20): 'Capricorn', range(20, 31): 'Aquarius'},          # Star Sign Dictionary, used to find star sign based on Birthday
                'february': {range(1, 19): 'Aquarius', range(19, 29): 'Pisces'},
                'march': {range(1, 21): 'Pisces', range(21, 31): 'Aries'},
                'april': {range(1, 20): 'Aries', range(20, 30): 'Taurus'},
                'may': {range(1, 21): 'Taurus', range(21, 31): 'Gemini'},
                'june': {range(1, 22): 'Gemini', range(22, 30): 'Cancer'},
                'july': {range(1, 23): 'Cancer', range(23, 31): 'Leo'},
                'august': {range(1, 23): 'Leo', range(23, 31): 'Virgo'},
                'september': {range(1, 23): 'Virgo', range(23, 30): 'Libra'},
                'october': {range(1, 24): 'Libra', range(24, 31): 'Scorpio'},
                'november': {range(1, 23): 'Scorpio', range(23, 30): 'Sagittarius'},
                'december': {range(1, 22): 'Sagittarius', range(22, 31): 'Capricorn'},
                }

    def __init__(self, root):

        fs1 = ttk.Style()  # Frame Styles
        fs1.configure('titleScreen.TFrame', background='purple')
        fs2 = ttk.Style()
        fs2.configure('information.TFrame', background='purple', relief='sunken')

        ls1 = ttk.Style()  # Text Styles
        ls1.configure('titleText.TLabel', font=('algerian', 48), background='purple', foreground='white', justify='center')
        ls2 = ttk.Style()
        ls2.configure('descriptiveText.TLabel', font='arial', background='purple', foreground='white', justify='center')
        ls3 = ttk.Style()
        ls3.configure('infoDisplay.TLabel', font='arial', background='purple', foreground='white', justify='left')

        root.title('Fortune Teller')

        self.mainframe = ttk.Frame(root, style='titleScreen.TFrame', padding='3 3 12 12')
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(self.mainframe, text='Fortune Teller', style='titleText.TLabel').grid(column=2, row=1, sticky=N)
        ttk.Label(self.mainframe, text='Welcome to the Fortune Teller.\nHere you can find out your star sign and what that says about you!', style='descriptiveText.TLabel').grid(column=2, row=2, sticky=N)
        ttk.Label(self.mainframe, text='Please enter your Birthday. (Example: 9 December)', style='descriptiveText.TLabel').grid(column=2, row=3, sticky=N)

        self.birthday = StringVar()
        birthdayEntry = ttk.Entry(self.mainframe, width=20, textvariable=self.birthday)
        birthdayEntry.grid(column=2, row=4, sticky=N)

        ttk.Button(self.mainframe, text="Look into the Crystal Ball", command=lambda: [self.starSignFinder(), self.showInfoScreen()]).grid(column=2, row=5, sticky=N)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        birthdayEntry.focus()

    def starSignFinder(self, *args):                    # Function that uses StarSign dict to work out star sign
        birthdayString = str(self.birthday.get())
        splitBirthday = birthdayString.split(' ')
        day = int(splitBirthday[0])
        month = splitBirthday[1]

        monthStarSign = self.starSign[month.lower()]

        for key in monthStarSign:
            if day in key:
                global personalStarSign 
                personalStarSign = monthStarSign[key]
                break

    def showInfoScreen(self):
        self.mainframe.destroy()
        infoScreen(root)


class infoScreen():

    starSignInfo = {'Aries': {'Strengths': 'hopeful, active, energetic, honest, versatile, brave, adventurous, passionate, generous, cheerful, argumentative, curious',     # TODO Put in info about other Star Signs
                              'Weaknesses': 'impulsive, naive, self-willed, belligerent, impatient',
                              'Symbol': 'Ram',
                              'Element': 'Fire',
                              'Sign Ruler': 'Mars',
                              'Lucky Colour': 'Red',
                              'Lucky Number': '5',
                              'Jewellery': 'Ruby',
                              'Best Match': 'Leo, Sagittarius and Aries'},

                    'Taurus': {'Strengths': 'romantic, decisive, logical, diligent, ardent, patient, talented in art, perseverant, benevolent',
                               'Weaknesses': 'prejudiced, dependent, stubborn',
                               'Symbol': 'Bull',
                               'Element': 'Earth',
                               'Sign Ruler': 'Venus',
                               'Lucky Colour': 'Pink',
                               'Lucky Number': '6',
                               'Jewellery': 'Emerald, Jade',
                               'Best Match': 'Capricorn, Virgo and Taurus'},

                    'Gemini': {'Strengths': 'multifarious, perspicacious, smart, cheerful, quick-witted, clement, charming',
                               'Weaknesses': 'fickle, gossipy, amphibian',
                               'Symbol': 'Twins',
                               'Element': 'Air',
                               'Sign Ruler': 'Mercury',
                               'Lucky Colour': 'Yellow',
                               'Lucky Number': '7',
                               'Jewellery': 'Opal',
                               'Best Match': 'Aquarius, Libra and Gemini'},

                    'Cancer': {'Strengths': 'with strong sixth sense, subjective, gentle, swift, imaginative, careful, dedicated, perseverant, kind, caring',
                               'Weaknesses': 'greedy, possessive, sensitive, prim',
                               'Symbol': 'Crab',
                               'Element': 'Water',
                               'Sign Ruler': 'Moon',
                               'Lucky Colour': 'Green',
                               'Lucky Number': '2',
                               'Jewellery': 'Pearl',
                               'Best Match': 'Pisces, Scorpio and Cancer'},

                    'Leo': {'Strengths': 'proud, charitable, reflective, loyal and enthusiastic',
                            'Weaknesses': 'arrogant, vainglorious, indulgent, wasteful, willful, and self-complacent',
                            'Symbol': 'Lion',
                            'Element': 'Fire',
                            'Sign Ruler': 'Sun',
                            'Lucky Colour': 'Red, Gold, Yellow',
                            'Lucky Number': '19',
                            'Jewellery': 'Gold',
                            'Best Match': 'Aries, Sagittarius and Leo'},

                    'Virgo': {'Strengths': 'helping, elegant, perfectionist, modest, practical, clearheaded',
                              'Weaknesses': 'picky, nosey, tortuous, confining',
                              'Symbol': 'Virgin maiden',
                              'Element': 'Earth',
                              'Sign Ruler': 'Mercury',
                              'Lucky Colour': 'Gray',
                              'Lucky Number': '7',
                              'Jewellery': 'Sapphire, Amber',
                              'Best Match': 'Sagittarius, Taurus and Gemini'},

                    'Libra': {'Strengths': 'idealistic, equitable, just, strong social skills, aesthetic, charming, artistic, beautiful, kind-hearted',
                              'Weaknesses': 'hesitant, narcissistic, lazy, perfunctory, freewheeling',
                              'Symbol': 'Scales',
                              'Element': 'Air',
                              'Sign Ruler': 'Venus',
                              'Lucky Colour': 'Brown',
                              'Lucky Number': '3',
                              'Jewellery': 'Coral, Amber',
                              'Best Match': 'Aquarius, Gemini and Libra'},

                    'Scorpio': {'Strengths': 'mysterious, rational, intelligent, independent, intuitive, dedicated, insightful, charming, sensible',
                                'Weaknesses': 'suspicious, fanatical, complicated, possessive, arrogant, self-willed, extreme',
                                'Symbol': 'Scorpion',
                                'Element': 'Water',
                                'Sign Ruler': 'Pluto, Mars',
                                'Lucky Colour': 'Purple, Black',
                                'Lucky Number': '4',
                                'Jewellery': 'Jasper, Black Crystal',
                                'Best Match': 'Cancer, Capricorn and Pisces'},

                    'Sagittarius': {'Strengths': 'insightful, superior, rational, brave, beautiful, lively, lovely, optimistic',
                                    'Weaknesses': 'forgetful, careless, rash',
                                    'Symbol': 'Archer',
                                    'Element': 'Fire',
                                    'Sign Ruler': 'Jupiter',
                                    'Lucky Colour': 'Light Blue',
                                    'Lucky Number': '6',
                                    'Jewellery': 'Amethyst',
                                    'Best Match': 'Virgo, Leo and Aries'},

                    'Capricorn': {'Strengths': 'excellent, intelligent, practical, reliable, perseverant, generous, optimistic, cute, persistent',
                                  'Weaknesses': 'stubborn, lonely, and suspicious',
                                  'Symbol': 'Goat',
                                  'Element': 'Earth',
                                  'Sign Ruler': 'Saturn',
                                  'Lucky Colour': 'Brown, Black, Dark Green',
                                  'Lucky Number': '4',
                                  'Jewellery': 'Black Jade',
                                  'Best Match': 'Virgo, Taurus and Pisces'},

                    'Aquarius': {'Strengths': 'original, tolerant, ideal, calm, friendly, charitable, independent, smart, practical',
                                 'Weaknesses': 'changeful, disobedient, liberalistic, hasty, rebel',
                                 'Symbol': 'Water carrier',
                                 'Element': 'Air',
                                 'Sign Ruler': 'Uranus',
                                 'Lucky Colour': 'Bronze',
                                 'Lucky Number': '22',
                                 'Jewellery': 'Black Pearl',
                                 'Best Match': 'Gemini, Libra and Aquarius'},

                    'Pisces': {'Strengths': 'conscious, aesthetic, platonic, dedicated, kind, with good temper',
                               'Weaknesses': 'recessive, sentimental, indecisive, unrealistic',
                               'Symbol': 'Fish',
                               'Element': 'Water',
                               'Sign Ruler': 'Neptune',
                               'Lucky Colour': 'White',
                               'Lucky Number': '11',
                               'Jewellery': 'Ivory Stone',
                               'Best Match': 'Scorpio, Cancer and Capricorn'},
                        }

    def __init__(self, root):

        self.fs1 = ttk.Style()  # Frame Styles
        self.fs1.configure('titleScreen.TFrame', background='purple')
        self.fs2 = ttk.Style()
        self.fs2.configure('information.TFrame', background='purple', relief='sunken')

        self.ls1 = ttk.Style()  # Text Styles
        self.ls1.configure('titleText.TLabel', font=('algerian', 48), background='purple', foreground='white', justify='center')
        self.ls2 = ttk.Style()
        self.ls2.configure('descriptiveText.TLabel', font='arial', background='purple', foreground='white', justify='center')
        self.ls3 = ttk.Style()
        self.ls3.configure('infoDisplay.TLabel', font='arial', background='purple', foreground='white', justify='left')

        mainframe = ttk.Frame(root, style='titleScreen.TFrame', padding='3 3 12 12')  # Main Frame
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.personalStarSignTitle = StringVar()
        self.personalStarSignTitle.set(personalStarSign)
        ttk.Label(mainframe, textvariable=self.personalStarSignTitle, style='titleText.TLabel').grid(column=1, row=1, sticky=N)  # User's Star Sign

        infoBundle = ttk.Frame(mainframe, style='titleScreen.TFrame', padding='3 3 12 12')  # Frame that contains Buttons and Display
        infoBundle.grid(column=1, row=2, sticky=N)

        infoOptions = ttk.Frame(infoBundle, style='titleScreen.TFrame', padding='3 3 12 12')  # Frame that contains Buttons
        infoOptions.grid(column=1, row=1, sticky=N)

        ttk.Button(infoOptions, text='Strengths', command=self.infoOptionsStrengths).grid(column=1, row=1, sticky=N)  # Info Buttons
        ttk.Button(infoOptions, text='Weaknesses', command=self.infoOptionsWeaknesses).grid(column=1, row=2, sticky=N)
        ttk.Button(infoOptions, text='Symbol', command=self.infoOptionsSymbol).grid(column=1, row=3, sticky=N)
        ttk.Button(infoOptions, text='Element', command=self.infoOptionsElement).grid(column=1, row=4, sticky=N)
        ttk.Button(infoOptions, text='Sign Ruler', command=self.infoOptionsSignRuler).grid(column=1, row=5, sticky=N)
        ttk.Button(infoOptions, text='Lucky Colour', command=self.infoOptionsLuckyColour).grid(column=1, row=6, sticky=N)
        ttk.Button(infoOptions, text='Lucky Number', command=self.infoOptionsLuckyNumber).grid(column=1, row=7, sticky=N)
        ttk.Button(infoOptions, text='Jewellery', command=self.infoOptionsJewellery).grid(column=1, row=8, sticky=N)
        ttk.Button(infoOptions, text='Best Match', command=self.infoOptionsBestMatch).grid(column=1, row=9, sticky=N)

        infoDisplay = ttk.Frame(infoBundle, width=450, height=300, style='information.TFrame', padding='5')  # Info Display
        infoDisplay.grid(column=2, row=1, sticky=(N, S, E, W))
        infoDisplay.grid_propagate(0)

        self.info = StringVar()
        ttk.Label(infoDisplay, textvariable=self.info, wraplength=450, style='infoDisplay.TLabel').grid(sticky=N)

        for child in infoOptions.winfo_children():  # Puts padding around each widget
            child.grid_configure(padx=5, pady=5)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def infoOptionsStrengths(self):
        self.info.set(self.starSignInfo[personalStarSign]['Strengths'])

    def infoOptionsWeaknesses(self):
        self.info.set(self.starSignInfo[personalStarSign]['Weaknesses'])

    def infoOptionsSymbol(self):
        self.info.set(self.starSignInfo[personalStarSign]['Symbol'])

    def infoOptionsElement(self):
        self.info.set(self.starSignInfo[personalStarSign]['Element'])

    def infoOptionsSignRuler(self):
        self.info.set(self.starSignInfo[personalStarSign]['Sign Ruler'])

    def infoOptionsLuckyColour(self):
        self.info.set(self.starSignInfo[personalStarSign]['Lucky Colour'])

    def infoOptionsLuckyNumber(self):
        self.info.set(self.starSignInfo[personalStarSign]['Lucky Number'])

    def infoOptionsJewellery(self):
        self.info.set(self.starSignInfo[personalStarSign]['Jewellery'])

    def infoOptionsBestMatch(self):
        self.info.set(self.starSignInfo[personalStarSign]['Best Match'])


root = Tk()
root.title('Fortune Teller')

homeScreen(root)
root.mainloop()