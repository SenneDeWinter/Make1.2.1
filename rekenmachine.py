#!/usr/bin/env python
"""
Een python rekenmachine script dat het volgende omvat:
    -Een zelf gemaakte python header
    -het script vraagt de gebruiker om 2 natuurlijke getallen in te geven
    -Deze 2 natuurlijke getallen vermeerderen, verminderen, vermenigvuldigen of delen
"""


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


def optellen(x, y):
    return x + y


def aftrekken(x, y):
    return x - y


def vermenigvuldigen(x, y):
    return x * y


def delen(x,y):
    return x / y

def main():
    print("REKENMACHINE, GEMAAKT DOOR SENNE")
    print("Kies wat je wilt doen")
    print("1: optellen")
    print("2: aftrekken")
    print("3: vermenigvuldigen")
    print("4: delen")

    while True:
        keuze = input("Vul je keuze in(1/2/3/4): ")

        if keuze in ('1', '2', '3', '4'):
            getal1 = int(input("Geef het eerste getal in: "))
            getal2 = int(input("Geef het tweede getal in: "))

            if keuze == '1':
                print(getal1, "+", getal2, "=", optellen(getal1, getal2))

            elif keuze == '2':
                print(getal1, "-", getal2, "=", aftrekken(getal1, getal2))

            elif keuze == '3':
                print(getal1, "*", getal2, "=", vermenigvuldigen(getal1, getal2))

            elif keuze == '4':
                print(getal1, "/", getal2, "=", delen(getal1, getal2))

            break
        else:
            print("Ongeldige invoer")

if __name__ == '__main__':    #code to execute if called from command-line
    main()






