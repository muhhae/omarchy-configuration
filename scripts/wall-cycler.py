#!/usr/bin/python3
from datetime import datetime
import subprocess

import time
import sys

icons = ["󰖔", "", "", "󰼱"]
suffixes = ["night", "morning", "day", "evening"]

HOUR = 60 * 60
MINUTE = 60

current_i = -1
offset = 2
DEBUG = 0


def WallCyclerDebug():
    global current_i
    h = 0
    while 1:
        i = (h % 24 + offset) % 24
        i = i / 24 * len(icons)
        i = int(i)
        print(f"{h % 24}: {i} :{icons[i]}")
        if i != current_i:
            subprocess.run(
                [
                    "omarchy-theme-bg-set",
                    f"/home/muhhae/bg-cycle/landscapes-tropic_island_{suffixes[i]}.jpg",
                ]
            )
            current_i = i

        h += 1
        sys.stdout.flush()
        time.sleep(1)


def WallCycler():
    global current_i
    while 1:
        h = datetime.now().hour
        i = (h + offset) % 24
        i = i / 24 * len(icons)
        i = int(i)
        if i != current_i:
            subprocess.run(
                [
                    "omarchy-theme-bg-set",
                    f"/home/muhhae/bg-cycle/landscapes-tropic_island_{suffixes[i]}.jpg",
                ]
            )
            current_i = i
        print(f"{icons[i]}")
        sys.stdout.flush()
        time.sleep(60)


if DEBUG:
    WallCyclerDebug()
else:
    WallCycler()
