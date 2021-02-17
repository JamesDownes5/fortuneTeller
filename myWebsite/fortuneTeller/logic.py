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

def Finder(birthday):                    # Function that uses StarSign dict to work out star sign
    splitBirthday = birthday.split(' ')
    day = int(splitBirthday[0])
    month = splitBirthday[1]

    monthStarSign = starSign[month.lower()]

    for key in monthStarSign:
        if day in key:
            personalStarSign = monthStarSign[key]
            break
        
    return personalStarSign
