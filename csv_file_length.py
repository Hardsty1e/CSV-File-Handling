# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 16:07:53 2021

@author: sanchit.thakur
"""

import csv

file = open("FC_Score_variable_Aug20.csv000")
reader = csv.reader(file)
lines= len(list(reader))
print(lines)
