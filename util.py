#!/usr/bin/python
# -*- coding: utf-8 -*-
"""util.py

基礎機能の分割

"""
import datetime, const, re
from datetime import datetime

# 保存先ディレクトリ名を取得
def getSaveDir() -> str:
    dt_now = datetime.datetime.now()
    year = dt_now.year
    month = dt_now.month
    saveDir = f"{const.DATA_DIRECTORY}/{year}_{month}"
    return saveDir

# 処理結果を通知するメッセージを表示する
# @input message str 本文
# @input type bool 
def systemMessage(message: str, type: bool) -> None:
    if type:
        print(f"成功：{message}")
    else:
        print(f"失敗：{message}")


def get_h_m(td):
    m, s = divmod(td.seconds, 60)
    h, m = divmod(m, 60)
    return h, m

# 勤務時間を足し算する
# @input timeA str XX:XX
# @input timeB str XX:XX
# @output str XX:XX
def addWorkTime(timeA: str, timeB: str) -> str:
    timeAList = re.findall(r"[0-9]+",timeA)
    timeBList = re.findall(r"[0-9]+",timeB)
    sumHour = int(timeAList[0]) + int(timeBList[0])
    sumMinute = int(timeAList[1]) + int(timeBList[1])
    if sumMinute >= 60:
        sumHour += (sumMinute // 60)
        sumMinute %= 60
    return f"{sumHour}:{sumMinute:02}"

# 退勤時間から残業時間を計算する
# @input clockOut str 退勤時間
# @output overTime str 残業時間
def calcOverTime(clockOut: str) -> str:
    FMT = "%H:%M"
    overTime = "0:00"
    if datetime.strptime(clockOut, FMT) >= datetime.strptime(const.ON_TIME, FMT):
        td = datetime.strptime(clockOut, FMT) - datetime.strptime(const.ON_TIME, FMT)
        h,m = get_h_m(td)
        # 定時後休憩を考慮する
        if h == 0:
            if m <= const.OVER_TIME_REST:
                m = 0
        overTime = (f"{h}:{m:02}")
    return overTime
    