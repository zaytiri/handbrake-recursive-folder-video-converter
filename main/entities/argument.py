

class Argument:
    """
    This class is responsible for creating a new object containing important information about an argument
    """
    def __init__(self, name, abrName, fullName):
        """
        initialization of important information about an argument
        :param name: the basic name of the argument
        :param abrName: the abbreviation of the name to use in the command line
        :param fullName: the full name to use in the command line
        """
        self.name = name
        self.abrName = abrName
        self.fullName = fullName
        self.value = None

    def set_argument_value(self, value):
        """
        sets the value for the current argument
        :param value: value the argument has
        """
        self.value = value
