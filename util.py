#!/usr/bin/python
# -*- coding: utf-8 -*-
"""util.py

基礎機能の分割

"""
import datetime, const

# 保存先ディレクトリ名を取得
def getSaveDir() -> str:
    dt_now = datetime.datetime.now()
    year = dt_now.year
    month = dt_now.month
    saveDir = f"{const.DATA_DIRECTORY}/{year}_{month}"
    return saveDir