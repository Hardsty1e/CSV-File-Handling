# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 13:51:55 2021

@author: sanchit.thakur
"""

import pandas as pd

chunk_size = 1000000    # Chunk Size
batch_no = 1

for chunk in pd.read_csv('File_name.csv', chunksize = chunk_size):
    chunk.to_csv('Filename' + str(batch_no) + '.csv', index = False)
    batch_no += 1
