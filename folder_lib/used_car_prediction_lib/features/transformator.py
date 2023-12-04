from abc import ABCMeta, abstractmethod
import numpy as np


class Transformator(metaclass = ABCMeta):
    @abstractmethod
    def transform(self,df,column_name:str):
        return NotImplementedError
    

class  Scaling_Normalization_Transformator(Transformator):
    """
    NormalizationTransformator normalizes our columns

    Methods:
        transform(self,df, column_name:str): DataFrame of interest and nromalized with columns
    """


    def transform(self,df, column_name:str):
        df[column_name] = (df[column_name] - df[column_name].min()) / (df[column_name].max() - df[column_name].min())
        return df


class Scaling_Standardization_Transformator(Transformator):
    """
    StandarizationTransformator standardalizes our columns

    Methods:
        transform(df,column_name:str): DataFrame of interest and standarized with columns
    """

    def __init__(self):
        pass

    def transform(self,df,column_name:str):
        df[column_name] = (df[column_name] - df[column_name].mean()) / df[column_name].std()
        return df



class Log_Transformator(Transformator):
    """
    NormalizationTransformator log our columns

    Methods:
        transform(df,column_name:str): DataFrame of interest and log with columns
    """

    def transform(self,df,column_name:str):
        df[column_name] = np.log(df[column_name])
        return df
    

class Square_Transformator(Transformator):
    """
    NormalizationTransformator log our columns

    Methods:
        transform(df,column_name:str): DataFrame of interest and log with columns
    """

    def transform(self,df,column_name:str):
        df[column_name] = np.square(df[column_name])
        return df
    

