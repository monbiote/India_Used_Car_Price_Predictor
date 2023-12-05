from abc import ABCMeta, abstractmethod
from pandas import read_csv
from sklearn.model_selection import train_test_split 


class Reader(metaclass = ABCMeta):
    
    @abstractmethod
    def read(self,file_path):
        return NotImplementedError
 ####################child################   
class CSVReader(Reader):

    def read(self,file_path):
        # Read the CSV file
        #pandas read_csv
        df = read_csv(file_path)
        # Return the DataFrame
        return df
    
    def split_df(self,df,trainSize=0.7):
        #split with test size
        train_data,test_data = train_test_split(df, trainSize)
        return train_data,test_data

 ####################child##################   