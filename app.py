#!/usr/bin/python
# -*- coding: utf-8 -*-
"""アプリケーション

アプリケーションの本体となりModelとViewの橋渡しを行う
'python app.py'で実行

"""
import os
import model, view
from util import *

def run():
    # 初期化処理
    # データ保存フォルダを作成する
    saveDir = getSaveDir()
    if not os.path.exists(saveDir):
        os.mkdir(saveDir)
    # ユーザーデータがない場合作成する
    for member in const.MEMBERS:
        user = model.User(member)
        if not user.isExist():
            user.create()
    
    view.modeSelectView()
    user = model.User("佐藤")
    if user.read():
        print(user.getName())
        print(user.getTotal())

if __name__ == '__main__':
    run()