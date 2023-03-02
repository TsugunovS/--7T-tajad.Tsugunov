from math import * 
from module1 import * 
#28/02/23
#В-7 Töötajad
#Зачетная работа по теме "Списки" и "Функции"
работники = ["Toomas", "Pavel", "Olja", "David", "Nastja", "Erik"]
год_рождения = [random.randint(1950, 2000)]

while True:
    print("Valige tegevus:")
    print("0 - Välju")
    print("1 - Sisestage töötajate arv ja nende aasta")
    print("2 - Pensionäride nimekiri")
    print("3 - Leidke töötajate keskmine vanus")
    print("4 - Noorimate töötajate nimekiri") # Молодые работники
    print("5 - Vanimate töötajate nimekiri") # Старые работники
    print("6 - Töötajate otsimine sünniaasta järgi")
    print("0 - Välju")
    valik = int(input("Sisestage number koos sobiva toiminguga: "))
    if valik == 1:
        tootajad()
    elif valik == 2:
        пенсионеры()
    elif valik == 3:
        keskmine_vanus()
    elif valik == 0:
        break
    else:
        print("Vale valik, proovige uuesti!") 
    if valik == 4:
        самые_молодые()
    elif valik == 5:
        самые_старые()
    elif valik == 6:
        поиск_работников_по_году_рождения(1990)
       
