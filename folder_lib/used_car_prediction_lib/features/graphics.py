from abc import ABCMeta, abstractmethod
import pandas as pd
import numpy as np

####################father################   
class Graphics(metaclass = ABCMeta):
    
    @abstractmethod
    def plotting_graphics(X_train, y_train, X_test, y_test):
        return NotImplementedError


####################child################   
class BinaryEncoder(Encoder): 

    #function for binary variables where we specify the true and false values
    def encoding_process(df, column_names: list, true_value, false_value):
        for column_name in column_names:
            df[column_name] = df[column_name].replace({true_value: 1, false_value: 0})
        return df

####################child################   
class CategoryOneHotEncoder(Encoder): 
    #function for categorical variables 
    def encoding_process(df, columns_to_encode):
        df = pd.get_dummies(df, columns=columns_to_encode, drop_first=True)
            
        # Convert Boolean columns to integers (0s and 1s)
        boolean_columns = df.select_dtypes(include='bool').columns
        df[boolean_columns] = df[boolean_columns].astype(int)
            
        return df

