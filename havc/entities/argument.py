

class Argument:
    """
    This class is responsible for creating a new object containing important information about an argument
    """
    def __init__(self, name, abbreviation_name, full_name, help_message, metavar, default='None'):
        """
        initialization of important information about an argument
        :param name: the basic name of the argument
        :param abbreviation_name: the abbreviation of the name to use in the command line
        :param full_name: the full name to use in the command line
        """
        self.name = name
        self.abbreviation_name = abbreviation_name
        self.full_name = full_name
        self.value = None
        self.help_message = help_message
        self.metavar = metavar
        self.default = default

    def set_argument_value(self, value):
        """
        sets the value for the current argument
        :param value: value the argument has
        """
        self.value = value


class Extensions(Argument):

    def set_argument_value(self, value):
        if not isinstance(value, list):
            if not value.startswith('.'):
                value = '.' + value
        else:
            for ext in value:
                if not ext.startswith('.'):
                    value[value.index(ext)] = '.' + ext

        self.value = value
