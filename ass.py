import pyttsx3

engine = pyttsx3.init()     # инициализация движка


engine.say('Кто по пивку ?')
engine.runAndWait()
# w = input()
engine.say(input())
engine.runAndWait()