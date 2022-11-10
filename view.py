#!/usr/bin/python
# -*- coding: utf-8 -*-
"""view.py

viewを提供する

"""
import const, util

# 区切り線
def section():
    print(const.SYMBOL * const.SYMBOL_LENGTH)

# アプリケーション起動View
def initialView() -> None:
    section()
    print("勤怠管理アプリ")
    section()

# モード選択View 
def modeSelectView() -> int:
    section()
    print("モードを選択してください")
    section()
    while True:
        for i, type in enumerate(const.MODE):
            print(f"{i}：{type}")
        mode = input(f"モード: ")
        if mode == "0" or mode == "1" or mode == "2":
            break
        else:
            print("\n選択肢から番号で入力してください。")
    return int(mode)