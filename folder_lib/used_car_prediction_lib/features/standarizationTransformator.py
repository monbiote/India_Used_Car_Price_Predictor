import transformator
import numpy as np
class StandarizationTransformator(transformator.Transformator):
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