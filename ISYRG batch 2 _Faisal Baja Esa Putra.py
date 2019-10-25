import wfdb
import numpy as np
import glob
import matplotlib.pyplot as plt

path_data = 'C:/Users/ACER/Downloads/ISYRG/mit-bih-arrhythmia-database-1.0.0/mit-bih-arrhythmia-database-1.0.0/200'

record = wfdb.rdrecord(path_data)
dict_record = record.__dict__

sinyal = wfdb.rdrecord(path_data)
sinyal_doc = sinyal.__dict__

data = wfdb.rdann(path_data, 'atr')
data_doc = data.__dict__

psignal =sinyal_doc["p_signal"]
psignal_0 =psignal[:,0]

plt.plot(range(360),psignal_0[:360])