from abc import ABCMeta, abstractclassmethod

class Reader(metaclass = ABCMeta):
    
    @abstractclassmethod
    def read(path):
        return NotImplementedError
