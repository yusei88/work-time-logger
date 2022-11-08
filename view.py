#!/usr/bin/python
# -*- coding: utf-8 -*-
"""view.py

viewを提供する

"""
import const

def section():
    print(const.SYMBOL * const.SYMBOL_LENGTH)

def initialView() -> None:
    section()
    print("勤怠管理アプリ")
    section()

def systemMessage(message: str, type: bool) -> None:
    if type:
        print(f"成功：{message}")
    else:
        print(f"失敗：{message}")
    
def modeSelectView() -> int:
    while True:
        section()
        print("モードの番号を選択してください")
        mode = input(f"{const.MODE} : ")
        if mode == "1" or mode == "2" or mode == "3":
            break
        else:
            print("モードの番号を入力してください。")
    return int(mode)