month = input('Enter the month:').lower()

day = int(input('Enter a number:'))
sign = 'month not selected'

if month == 'january' and 21 <= day <= 31 or month=='february'and 1 <= day <= 19:
  sign = 'aquarius' # водолей
elif month=='february' and 20 <= day <= 29 or month == 'march' and 1 <= day <=20:
  sign = 'Pisces' # рыбы
elif month=='march' and 21 <= day <= 31 or month=='april' and 1 <= day <= 20:
  sign = 'Aries' #овен
elif month=='april' and 21 <= day <= 30 or month=='may' and 1 <= day <= 21:
  sign = 'Taurus' #телец
elif month=='may' and 22 <= day <= 31 or month=='june' and 1 <= day <= 21:
  sign = 'Gemini' #близн
elif month=='june' and 22 <= day <= 30 or month=='july' and 1 <= day <= 23:
  sign = 'Cancer' #рак
elif month=='july' and 24 <= day <= 31 or month=='august' and 1 <= day <= 23:
  sign = 'Leo' #лев
elif month=='august' and 24 <= day <= 31 or month=='september' and 1 <= day <= 23:
  sign = 'Virgo' #дева
elif month=='september' and 24 <= day <= 30 or month=='october' and 1 <= day <= 23:
  sign = 'Libra' #весы
elif month=='october' and 24 <= day <= 31 or month=='november' and 1 <= day <= 22:
  sign = 'Scorpio' #скорп
elif month=='november' and 23 <= day <= 30 or month=='december' and 1 <= day <= 21:
  sign = 'Sagittarius' #стрелец
elif month=='december' and 22 <= day <= 31 or month=='january' and 1 <= day <= 20:
  sign = 'Capricorn' #козерог
else:
  print('error in the name of the month')

print(f'Your zodiac sign: {sign}.')