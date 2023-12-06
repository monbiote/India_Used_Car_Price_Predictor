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

    def split_df(self,X,y,test_size=0.3, random_state=123):
        #split with test size
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=test_size, random_state=random_state)
        return X_train, X_test, y_train, y_test

 ####################child##################   