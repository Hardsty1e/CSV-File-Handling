# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 17:25:41 2021

@author: sanchit.thakur.in
"""

import pandas as pd

dataframe1 = pd.read_csv("File_name.csv000")

dataframe1.to_csv("File_name.csv", index = False)     # index = false, otherwise new empty row will be added on top
