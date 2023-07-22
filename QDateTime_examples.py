#! /usr/bin/env python3
"""Created by chris at 7/21/23


Ref: 
"""
# raise NotImplementedError
from PyQt5.QtCore import QDateTime, QDate, QTime

sss = "2022:08:10"
format = "yyyy:MM:dd"

# Create QDateTime objects
curDT = QDateTime.currentDateTime()
print(f"current date and time: {curDT}")
print(f"current date and time: {curDT.toString(format)}")
print(f"current date and time: {curDT.toString()}")
print()

qdate = QDate(2023, 8, 20)
print(f"date: {qdate}")

qtime = QTime(17, 35, 20)
print(f"time: {qtime}")

qdatetime = QDateTime(qdate, qtime)
# qdatetime = QDateTime(2023,8,20,18,1,2)
# QDateTime(year, month, day, hour, minute, second
print(f"datetime: {qdatetime}")
print()

# Parsing from a string
# see obsidian: [[RPG - QDateTime format]]
date_from_format = QDate.fromString(sss, format)
print(f"date from format: {date_from_format}")

if __name__ == "__main__":
    pass
