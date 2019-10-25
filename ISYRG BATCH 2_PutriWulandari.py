# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:04:30 2019

@author: Putri
"""

import wfdb
import numpy as np
import glob
import matplotlib.pyplot as plt

path_data = 'C:/Users/Putri/Documents/AI SYS/arrhythmia-database-/102'

record = wfdb.rdrecord(path_data)
dict_record = record.__dict__

data = wfdb.rdann(path_data, 'atr')
data_doc = data.__dict__

psignal =dict_record["p_signal"]
psignal_0 =psignal[:,0]

plt.plot(range(360),psignal_0[:360])
