from abc import ABCMeta, abstractclassmethod

class Reader(metaclass = ABCMeta):
    
    @abstractclassmethod
    def read(path):
        return NotImplementedError

import pandas as pd
from sklearn.model_selection import train_test_split 


class CSVReader(Reader):

    def read(path):
        data = pd.read_csv(path)

        #split with test size
        trainSize = 0.83
        train_data,text_data = train_test_split(data, trainSize)
        return train_data,text_data