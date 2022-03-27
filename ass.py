import pyttsx3

engine = pyttsx3.init()     # инициализация движка

engine.setProperty('rate', 150)     # скорость речи
engine.setProperty('volume', 0.9)   # громкость (0-1)

engine.say('Кто по пивку ? А?')
engine.runAndWait()
