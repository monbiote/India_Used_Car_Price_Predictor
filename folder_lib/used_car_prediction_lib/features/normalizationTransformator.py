import transformator


class NormalizationTransformator(transformator.Transformator):
    """
    NormalizationTransformator normalizes our columns

    Methods:
        transform(data,columns): DataFrame of interest and nromalized with columns
    """


    def __init__(self):
        pass


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
