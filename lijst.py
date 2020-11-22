#!/usr/bin/env python
"""
Een python script dat eerst een voorgeprogrammeerde lijst weergeeft, daarna om een willekeurig aantal woorden vraagt en
deze ook in een lijst steekt en weergeeft.
"""


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


lijst = ["AP, Hogeschool, heeft, ons, genaaid"]
print(lijst)
woorden = input("Geef een willekeurig aantal woorden in om de lijst aan te vullen")


def main():
    lijst.append(woorden)
    print(lijst)

if __name__ == '__main__':    #code to execute if called from command-line
    main()