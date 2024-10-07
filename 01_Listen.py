'''Aufgabe 1: Listen
Mache dich im Python-Interpreter mit dem Umgang mit Listen vertraut. Kapitel 2.6 im Skript (S.41) enthält nützliche Informationen.
(a) Lege eine Liste mit Namen "zahlen" an, die mindestens 10 Elemente enthält.
'''
zahlen = [1,2,3,4,5,6,7,8,9,10]
# b) Gib das 7. Element der Liste aus.
print(zahlen[6], " ist das 7. Element der Liste")

#c) Gib das 2.-8. Element der Liste als Liste aus.
print("2.-8. Element der Liste: ", zahlen[1:8])

#d) Gib das 2.-8. Element der Liste als einzelne Elemente aus.
print("Gib das 2.- 8. Element der Liste als einzelne Elemente aus.")
for i in range(1,8):
    print(zahlen[i])

#e) Füge die Zahlen 15, 23 und 95 zur Liste hinzu.

print("Liste ohne die neuen Zahlen: ", zahlen)
zahlen.append(15)
zahlen.append(23)
zahlen.append(95)
print("Liste mit den neuen Zahlen: ", zahlen)

#f) Lösche das 3. Element der Liste

del zahlen[2]
print("Liste nachdem das dritte Element gelöscht wurde: ", zahlen)

#g) Lösche die Zahl 23 aus der Liste
zahlen.remove(23)
print("Liste nachdem die Zahl 23 entfernt wurde: ", zahlen)