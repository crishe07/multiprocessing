#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 09:16:23 2023

@author: Ezquerro
"""

from time import sleep
from random import random

from multiprocessing import Process

def f():
    for i in range(5):
        print ("hola",i)
        sleep(random())
        
if __name__=="__main__":
    p=Process(target=f)
    q=Process(target=f)
    p.start()
    q.start()
    print("fin")
