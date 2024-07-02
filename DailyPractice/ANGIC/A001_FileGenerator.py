from abc import ABCMeta


class FileBase(ABCMeta):
    """Class to represent the data structure for for specific medical enrollment files
    
    The class incorporate the other classes' objects to handle generation, writing, and parsing functionalities"""