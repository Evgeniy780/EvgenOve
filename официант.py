# свободный проект 1
# афициант диалог с клинтами
import datetime
import pyttsx3
ofi = pyttsx3.init()
ofi.setProperty('rate', )
today = datetime.datetime.today()
w = today.strftime("%H.%M")
choice = "из чего состоит 1." \
         "сколько стоит 2." \
         "по наличию 3. " \
         "если вы хотите ознакомиться с полной информацией 4." \
         "если вы готовы сделать заказ 5." \
         "выйход из программы 0"
ofi.say(choice)
ofi.runAndWait()
# обеденное меню
obed = {'первое': [['','','',5]],
          'напитки': [['', 'масло', 'сахар'], 4, 1025],
            'пицца': [['котлета по киевски', 'пельмени', 'блины с ветчиной и сыром'], 5, 985],
          'суши': [['цезарь', 'летний', 'олевье'], 5, 985],
        '': [['цезарь', 'летний', 'олевье'], 5, 985]}
menu = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
          'медовик': [['мука', 'масло', 'сахар'], 4, 1025],
          'киевский': [['сахар', 'мука', 'масло'], 5, 985]}
zav = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
          'медовик': [['мука', 'масло', 'сахар'], 4, 1025],
        ',блинчики': [['тесто', 'масло', 'сахар'], 4, 1025],
        'олади': [['мука', 'масло', 'сахар'], 4, 1025],
          'киевский': [['сахар', 'мука', 'масло'], 5, 985]}
# disert = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
#           'медовик': [['мука', 'масло', 'сахар'], 4, 1025],
#           'киевский': [['сахар', 'мука', 'масло'], 5, 985]}
# Вступительная речь
ofi.setProperty('rate', 999)
today = datetime.datetime.today()
w = today.strftime("%H.%M")
# if 9.00 < float(w) < 11.00 or 11.00 < float(w) < 16.00 or 16.00 < float(w) < 23.00:


if 9.00 < float(w) < 11.00:
    ofi.say(f"доброе утро. ознакомьтесь с меню завтра. при заказе дисерта кофе в подарок")
    ofi.runAndWait()
    for k, v in zav.items():
        wish = int(input(": "))
        if wish == 1:
            print(f"Торт {k} состоит из {v[0]}")
            ofi.say(f'Торт {k} состоит из {v[0]}')
            ofi.runAndWait()
        elif wish == 2:
            print(f"Торт {k} стоит {v[1]} рублей")
            ofi.say(f"Торт {k} стоит {v[1]} рублей")
            ofi.runAndWait()
        elif wish == 3:
            print(f"Торт {k} осталось {v[-1]} грамм")
            ofi.say(f"Торт {k} осталось {v[-1]} грамм")
            ofi.runAndWait()
        elif wish == 4:
            print(f"полное наименование с составом{k},{v}")
            ofi.say(f"полное наименование с составом{k},{v}")
            ofi.runAndWait()
        elif wish == 5:
            weight = int(input(" Сколько торта Вам положить: "))
            print(f"к оплате {zav[k][1] * weight / 100}")
            print(f"торта {k} осталось {v[2] - weight} грамм")
            ofi.say(f"к оплате {zav[k][1] * weight / 100},")
            ofi.runAndWait()
        elif wish == 0:
            ofi.say('досвиданья')
            ofi.runAndWait()
            break
        else:
            print('сделайте ваш выбор')

elif 11.00 < float(w) < 16.00:
    ofi.say("Добрый день. ")
    ofi.runAndWait()
elif 16.00 < float(w) < 23.00:
    ofi.say("Добрый вечер.")
    ofi.runAndWait()
else:
    ofi.say("здравствуйте. извините мы закрыты")
    ofi.runAndWait()

for k, v in obed.items():
    if wish == 1:
        print(f"Торт {k} состоит из {v[0]}")
        engine.say(f'Торт {k} состоит из {v[0]}')
        engine.runAndWait()
    elif wish == 2:
        print(f"Торт {k} стоит {v[1]} рублей")
        engine.say(f"Торт {k} стоит {v[1]} рублей")
        engine.runAndWait()
    elif wish == 3:
        print(f"Торт {k} осталось {v[-1]} грамм")
        engine.say(f"Торт {k} осталось {v[-1]} грамм")
        engine.runAndWait()
    elif wish == 4:
        print(f"{k},{v}")
        engine.say(f"{k},{v}")
        engine.runAndWait()
    elif wish == 5:
        weight = int(input(" Сколько торта Вам положить: "))
        print(f"к оплате {pastry[k][1] * weight / 100}")
        print(f"торта {k} осталось {v[2] - weight} грамм")
        engine.say(f"к оплате {pastry[k][1] * weight / 100},")
        engine.runAndWait()
# print(today.strftime("%Y.%m.%d.%H.%M.%S"))
# vs_r = "Добрый вечер"
# rech = "Привет"
# ofi.say(w)
ofi.runAndWait()