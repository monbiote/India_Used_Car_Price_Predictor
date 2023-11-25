from abc import ABCMeta, abstractclassmethod

class Transformator(metaclass = ABCMeta):
    @abstractclassmethod
    def transform(self,data,columns):
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