import datetime

import random

def tootajad():
    n = int(input("Sisestage tööliste hulk: "))
    год_рождения = []
    names = ["Toomas", "Pavel", "Olja", "David", "Nastja", "Erik"]
    работники = random.sample(names, n)
    for i in range(n):
        год = random.randint(1950, 2000)
        год_рождения.append(год)
        print(f"Sisestage sünniaasta töötajale {работники[i]}: {год}")
    return работники, год_рождения

#def tootajad():
#    n = int(input("Sisestage tööliste hulk: "))
#    работники = []
#    год_рождения = []
#    for i in range(n):
#        имя = input(f"Sisestage nimi töötliste n{i+1}: ")
#        год = int(input(f"Sisestage töötaja sünniaasta n{i+1}: "))
#        работники.append(имя)
#        год_рождения.append(год)
#    return работники, год_рождения

def пенсионеры():
    работники, год_рождения = tootajad()
    текущий_год = datetime.datetime.now().year
    пенсионеры = [работники[i] for i in range(len(работники)) if текущий_год - год_рождения[i] >= 60]
    print("Список пенсионеров:")
    for пенсионер in пенсионеры:
        print(пенсионер)


def keskmine_vanus():
    работники, год_рождения = tootajad()
    текущий_год = datetime.datetime.now().year
    возрасты = [текущий_год - год_рождения[i] for i in range(len(работники))]
    средний_возраст = sum(возрасты) / len(работники)
    print(f"Keskmine töötaja vanus on {средний_возраст:.1f} aastat")


def самые_молодые():
    работники, год_рождения = tootajad()
    список_работников = []
    возраст_года = 30  # устанавливаем возраст молодых рабоников
    name = set()  
    for i in range(len(работники)):
        if 2023 - год_рождения[i] <= возраст_года: 
            name.add(работники[i])  
    print("Список самых молодых работников:")
    for имя in name:
        print(имя)


def самые_старые():
    работники, год_рождения = tootajad()
    список_работников = []
    возраст_года = 40  # устанавливаем возраст старых рабртников
    name = set()  # создаем пустое множество для уникальных имен
    for i in range(10):
        max_year = max(год_рождения)
        max_index = год_рождения.index(max_year)
        if 2023 - max_year >= возраст_года:  
            name.add(работники[max_index]) 
        год_рождения[max_index] = -1  
    print("Список самых старых работников:")
    for имя in name:
        print(имя)


def поиск_работников_по_году_рождения(год):
    работники, год_рождения = tootajad()
    результаты_поиска = []
    for i in range(len(работники)):
        if год_рождения[i] == год:
            результаты_поиска.append(работники[i])
    if len(результаты_поиска) > 0:
        print(f"Работники, родившиеся в {год} году:")
        for работник in результаты_поиска:
            print(работник)
    else:
        print(f"Работников, родившихся в {год} году, нет в списке.")





