import pycountry
import phonenumbers
from phonenumbers import carrier, timezone, region_code_for_number
import requests
import urllib3
from bs4 import BeautifulSoup
import re
import colorama
from colorama import Fore, Back, Style

demon = '''


                   ██           ██
                  ████         ████
                 ██████       ██████
                ████████     ████████
               ██████████   ██████████
              ███████████ _ ███████████
              ██████████████████████████
             ██████ ██████████████ █████
  █ █       ███████   ███████████  ██████    █  █  █
  █ █  █    ███████    ████████    ██████     █ █ █
█ █ █ █    ████████      ████      ███████    █████
 █████     ████████   █ █████  █  ████████ ███████
 ████████  █████████    ██████    ██████████   ███
    ██    ███████████████████████████████ ██    ██
    █     ███ ██████████████████████████  ██
          ███  ████████████████████████  ███
          ███  ████████████████████████  ███
           ███     ████████████████     ██
            ██        ██████████       ██
             ███      ███    ███       █
               ██     ██      ██      █
                ███   █        █     █
                   ███              █
                      █████████████

'''

print(demon)

print('''
 █     █░ █    ██  ▄▄▄██▀▀ ▄▄▄      ██▀███  
▓█░ █ ░█░ ██  ▓██▒   ▒██  ▒████▄   ▓██ ▒ ██▒
▒█░ █ ░█ ▓██  ▒██░   ░██  ▒██  ▀█▄ ▓██ ░▄█ ▒
░█░ █ ░█ ▓▓█  ░██░▓██▄██▓ ░██▄▄▄▄██▒██▀▀█▄  
░░██▒██▓ ▒▒█████▓  ▓███▒  ▒▓█   ▓██░██▓ ▒██▒
░ ▓░▒ ▒  ░▒▓▒ ▒ ▒  ▒▓▒▒░  ░▒▒   ▓▒█░ ▒▓ ░▒▓░
  ▒ ░ ░  ░░▒░ ░ ░  ▒ ░▒░  ░ ░   ▒▒   ░▒ ░ ▒░
  ░   ░   ░░░ ░ ░  ░ ░ ░    ░   ▒     ░   ░ 
    ░       ░      ░   ░        ░     ░     

''')


# Отключение проверки сертификата SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
RE_ANSI = re.compile(r'\x1B(?:[@-Z\-_]|\[[0-?]*[ -/]*[@-~])')


class PhoneNumber:
    print('[1]', end = "")
    print(' Пробив по номеру')
    def __init__(self):
        self.number = input(Fore.WHITE +'[+]' + Fore.RED+  ' Введите номер телефона с + без пробелов: ')
        self.output()

    def default_info(self):
        try:
            phone_num = phonenumbers.parse(self.number, None)
        except:
            raise ValueError('Номер введён неверно')

        country_iso = region_code_for_number(phone_num)
        country = pycountry.countries.get(alpha_2=country_iso)

        operator = carrier.name_for_number(phone_num, None)
        if operator == '':
            operator = 'Не найдено'

        timezone_info = timezone.time_zones_for_number(phone_num)
        if len(timezone_info) > 1:
            timezone_info = f'{len(timezone_info)} штук'
        elif len(timezone_info) == 1:
            timezone_info = ''.join(timezone_info)

        out = {
            'country': country.name,
            'operator': operator,
            'timezone': timezone_info
        }

        return out

    def output(self):
        data = self.default_info()
        print(Fore.RED + f'''
=====================================
{Style.RESET_ALL}
        ''',end = "")
        print(Fore.GREEN + f'''
   Номер:         {self.number}
   Страна:        {data['country']}
   Оператор:      {data['operator']}
   Часовой пояс:  {data['timezone']}
{Style.RESET_ALL}
        ''')
        self.number = self.number[1:]
        url = f"https://tlfbase.ru/phone={self.number}"
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            soup = BeautifulSoup(response.text, 'html.parser')
            # Получаем текст из ответа и разбиваем его на строки
            lines = response.text.split('\n')
            # Проверяем, есть ли 116-ая и 110-ая строки
            if len(lines) >= 116 and len(lines) >= 110:
                line_116 = lines[115]  # Индекс 115 соответствует 116-ой строке
                line_110 = lines[109]  # Индекс 109 соответствует 110-ой строке
                # Используем Beautiful Soup для извлечения текста из HTML-тегов
                soup_116 = BeautifulSoup(line_116, 'html.parser')
                soup_110 = BeautifulSoup(line_110, 'html.parser')
                text_116 = soup_116.get_text(strip=True)
                text_110 = soup_110.get_text(strip=True)
                print(Fore.GREEN +" ", '', text_116)
                print()
                print(Fore.RED + f'''
=====================================
{Style.RESET_ALL}
        ''',end = "\n")
        print()


colorama.init()
PhoneNumber()
