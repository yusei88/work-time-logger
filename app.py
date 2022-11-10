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
    view.initialView()
    # 初期化処理
    # データ保存フォルダを作成する
    saveDir = getSaveDir()
    if not os.path.exists(saveDir):
        os.mkdir(saveDir)
        view.systemMessage("今月のフォルダを作成",const.TYPE_NORMAL)
    # ユーザーデータがない場合作成する
    for member in const.MEMBERS:
        user = model.User(member)
        if not user.isExist():
            view.systemMessage(f"{member}さんのファイルを作成",user.create())
    
    mode = view.modeSelectView()
    print(f"「{mode}:{const.MODE[mode]}」が選択されました。")
    

if __name__ == '__main__':
    run()