# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 13:51:55 2021

@author: sanchit.thakur.in
"""

import pandas as pd

chunk_size = 1000000    # Chunk Size
batch_no = 1

for chunk in pd.read_csv('FC_Score_variable_Sep20.csv', chunksize = chunk_size):
    chunk.to_csv('FC_Score_variable_Sep20_' + str(batch_no) + '.csv', index = False)
    batch_no += 1
