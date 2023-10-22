import urllib.request
import json
import webbrowser
import colorama
from colorama import Fore, Back, Style

colorama.init()

def phone_info_main(phone):
    getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone  # формируем запрос

    try:
        infoPhone = urllib.request.urlopen(getInfo)  # открываем запрос
        infoPhone = json.load(infoPhone)
        print("        ШОКОЛАДНЫЙ ГЛАЗ БОБИКА")
        print('''
---------------------------------------
|        ''')
        print("|")
        print("|Номер телефона", "+" + phone)
        print("|Страна", infoPhone["country"]["name"])
        print("|Регион", infoPhone["region"]["name"])
        print("|Город", infoPhone["0"]["name"])
        print("|Оператор", infoPhone["0"]["oper"])
        print("|Часть света", infoPhone["country"]["location"])
        print("|")
        print('''|
----------------------------------------
        ''')

    except Exception as e:
        print("Телефон не найден")

z = input(Fore.WHITE +'[+]' + Fore.RED+  ' Введите номер телефона без +: ')
phone_info_main(z)
