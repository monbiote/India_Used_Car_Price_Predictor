from abc import ABCMeta, abstractmethod
import numpy as np


class Transformator(metaclass = ABCMeta):
    @abstractmethod
    def transform(self,df,column_name:str):
        return NotImplementedError
    

class NormalizationTransformator(Transformator):
    """
    NormalizationTransformator normalizes our columns

    Methods:
        transform(data,columns): DataFrame of interest and nromalized with columns
    """


    def transform(self,data,columns):
        for c in columns:
            min_value = min(data[c])
            max_value = max(data[c])
            normalized_c = []

            for value in data[c]:
                normalized_value = (value - min_value)/(max_value - min_value)
                normalized_c.append(normalized_value)
            data[c] = normalized_c
        return data


class StandarizationTransformator(Transformator):
    """
    StandarizationTransformator normalizes our columns

    Methods:
        transform(data,columns): DataFrame of interest and standarized with columns
    """

    def __init__(self):
        pass

    def transform(data,columns):
        for c in columns:
            data[c] = (data[c]-np.mean)/np.std(data[c])
        return data



class NormalizationTransformator(Transformator):
    """
    NormalizationTransformator normalizes our columns

    Methods:
        transform(data,columns): DataFrame of interest and nromalized with columns
    """



    def transform(data,columns):
        for c in columns:
            min_value = min(data[c])
            max_value = max(data[c])
            normalized_c = []

            for value in data[c]:
                normalized_value = (value - min_value)/(max_value - min_value)
                normalized_c.append(normalized_value)
            data[c] = normalized_c
        return data
    


class Square_Transformator(Transformator):
    """
    SquareTransformator transform our columns

    Methods:
        transform(data,columns): DataFrame of interest and nromalized with columns
    """

    def transform(df,column_name:str):
        df[column_name] = np.square(df[column_name])
        return df
    

