#!/usr/bin/python
# -*- coding: utf-8 -*-
"""model.py

モデル定義

"""
import json, os
from util import *

class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.dir = getSaveDir()
        self.fileName = f"{self.dir}/{name}.json"
    
    def isExist(self) -> bool:
        return os.path.exists(self.fileName)

    def create(self) -> bool:
        try:
            with open(self.fileName, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "name": self.name,
                        "total": "",
                        "ave": "",
                        "prediction": "",
                        "dairy": []
                    }, f
                )
        except:
            return False
        else:
            return True
    
    def read(self) -> bool:
        try:
            with open(self.fileName, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except:
            return False
        else:
            self.setName(self.data['name'])
            self.setTotal(self.data['total'])
            self.setAve(self.data['ave'])
            self.setPrediction(self.data['prediction'])
            self.setDairy(self.data['dairy'])
            return True
    
    # ゲッター
    def getName(self) -> str:
        return self.name
    def getTotal(self) -> str:
        return self.total
    def getAve(self) -> str:
        return self.ave
    def getPrediction(self) -> str:
        return self.prediction
    def getDairy(self) -> dict:
        return self.dairy
    
    # セッター
    def setName(self, name) -> None:
        self.name = name
    def setTotal(self, total) -> None:
        self.total = total
    def setAve(self, ave) -> None:
        self.ave = ave
    def setPrediction(self, prediction) -> None:
        self.prediction = prediction
    def setDairy(self, dairy) -> None:
        self.dairy = dairy