import wfdb
import numpy as np
import glob
import matplotlib.pyplot as plt

path_data = 'C:/Users/USER/ISYSRG/Dataset/mit-bih-arrhythmia-database-1.0.0/124'

record = wfdb.rdrecord(path_data)
dict_record = record.__dict__

attribute = wfdb.rdann(path_data,'atr')
attribute_record= attribute.__dict__

signal = dict_record['p_signal'][:,0]

fig,ax1=plt.subplots(nrows=1)
ax1.plot(np.arange(1440), signal[0:1440])