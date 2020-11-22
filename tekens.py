#!/usr/bin/env python
"""
Een python script dat als output het aantal tekens geeft van de ingegeven string.
Het script vraagt om een willekeurig woord in te geven en geeft als output het aantal tekens terug.
"""


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


woord = input("Geef een willekeurig woord: ")


def main():
    print(f"Het woord: {woord} is",len(woord),"tekens lang")

if __name__ == '__main__':    #code to execute if called from command-line
    main()