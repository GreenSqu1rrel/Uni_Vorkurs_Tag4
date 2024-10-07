'''Aufgabe 2: Funktionen
Schreibe eine Funktion, die eine Liste von Zahlen entgegennimmt und
a) das kleinste Element der Liste ausgibt'''

def kleinstesElement(liste):
    tmp = liste[0]
    for i in range (0,len(liste)):
        if liste[i] < tmp:
            tmp = liste[i]
            print("New temp: ", tmp)
    print("Kleinstes Element ist ", tmp)
    return tmp

def groesstesElement(liste):
    tmp = liste[0]
    for i in range (0,len(liste)):
        if liste[i] > tmp:
            tmp = liste[i]
            print("New temp: ", tmp)
    print("Groesstes Element ist ", tmp)
    return tmp

def durch5teilbar(liste):
    tmp = []
    for i in range (0,len(liste)):
        if liste[i] % 5 == 0:
            tmp.append(liste[i])
            print(liste[i], " ist durch 5 teilbar.")
    return tmp

def durchBeliebigTeilbar(liste):
    tmp = []
    teilbar = int(input("Die Zahl, durch die geteilt werden soll: "))
    for i in range (0,len(liste)):
        if liste[i] % teilbar == 0:
            tmp.append(liste[i])
            print(liste[i], " ist durch ", teilbar, " teilbar.")
    return tmp

from random import randint, random
#Random Liste erstellen
randomliste = []
for i in range(30):
    m = randint(1, 100)
    randomliste.append(m)
print(randomliste)#und ausgeben
while True:
    match input("Welche Aufgabe soll erledigt werden? "):
        case "a":
            print(kleinstesElement(randomliste))
        case "b":
            print(groesstesElement(randomliste))
        case "c":
            print(durch5teilbar(randomliste))
        case "d":
            print(durchBeliebigTeilbar(randomliste))
        case "stop":
            False
