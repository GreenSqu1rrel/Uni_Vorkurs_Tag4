'''Aufgabe 3 Namensräume und Shadowing
folgender Programmcode ist gegeben:'''
x = "foo"
def x():
    x = "bar"
    print(x)
print(x)
'''Was wird das Programm ausgeben?
a) Das Programm terminiert mit einem Fehler.
b) Das Programm gibt zuerst “bar”, dann “foo” aus.
c) Das Programm gibt etwas wie “<function x at 0x100495578 >” aus.
d) Das Programm gibt nur “foo” aus.

c ist richtig, weil x überschrieben wird und die funktion auf sich selber referiert.
'''
x = "foo"
def test():
    x = "bar"
    print(x)
print(x)

#foo wird ausgegeben, weil die Methode nicht aufgerufen wird.