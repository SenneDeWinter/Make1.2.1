#!/usr/bin/env python
"""
Een python script dat het volgende doet:
    -vraagt achter je leeftijd
    -berekent in welk jaar je geboren bent en dat ook als output meegeeft
    -berekent in welk jaar je 50 jaar zal zijn en dat ook als output meegeeft
"""


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


leeftijd = int(input("Hoe oud ben je? "))


def main():
    if leeftijd < 50:
        print(f"Je bent geboren in het jaar {2020 - leeftijd}, je wordt 50 in het jaar {(2020 - leeftijd) + 50} ")

    elif leeftijd > 50:
        print(f"Je bent geboren in het jaar {2020 - leeftijd}, je werd 50 in het jaar {(2020 - leeftijd) + 50} ")




if __name__ == '__main__':    #code to execute if called from command-line
    main()