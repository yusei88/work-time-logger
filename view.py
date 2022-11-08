#!/usr/bin/python
# -*- coding: utf-8 -*-
"""view.py

viewを提供する

"""
import const

def modeSelectView() -> int:
    while True:
        print("*"*50)
        print("モードの番号を選択してください")
        mode = input(f"{const.MODE} : ")
        print("*"*50)
        if mode == "1" or mode == "2" or mode == "3":
            break
        else:
            print("モードの番号を入力してください。")
    return int(mode)