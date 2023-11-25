from abc import ABCMeta,abstractclassmethod

class Preprocessor(metaclass = ABCMeta):

    @abstractclassmethod
    def preprocess(train_data, column):
        return NotImplementedError
    