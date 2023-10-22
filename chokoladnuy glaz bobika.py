import urllib.request
import json
import webbrowser


def phone_info_main(phone):
    getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone  # формируем запрос

    try:
        infoPhone = urllib.request.urlopen(getInfo)  # открываем запрос
        infoPhone = json.load(infoPhone)
        print('''
=======================================
        ''')

        print("Номер телефона", "+" + phone)
        print("Страна", infoPhone["country"]["name"])
        print("Регион", infoPhone["region"]["name"])
        print("Город", infoPhone["0"]["name"])
        print("Оператор", infoPhone["0"]["oper"])
        print("Часть света", infoPhone["country"]["location"])
        print('''
=======================================
        ''')

    except Exception as e:
        print("Телефон не найден")


phone_info_main()
