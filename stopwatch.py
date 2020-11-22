#!/usr/bin/env python
"""
Een python script dat de functie van een stopwatch heeft
"""


import time


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Tijd = {0}:{1}:{2}".format(int(hours), int(mins),sec))

input("Druk op enter om te starten")
start_time= time.time()

input("Druk op enter op te stoppen")
end_time = time.time()

time_lapsed = end_time - start_time
time_convert(time_lapsed)