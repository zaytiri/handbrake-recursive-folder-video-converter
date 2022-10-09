import argparse


class ArgumentsService:
    """
    This class is responsible for encapsulating the how-to of parsing arguments
    """
    def __init__(self, prog=None, usage=None, description=None, epilog=None):
        """
        Initialize argument parser from chosen library.
        :param prog: the name of the program
        :param usage: description of the program usage
        :param description: text to display before the argument help
        :param epilog: text to display after the argument help
        """
        self.parser = argparse.ArgumentParser(prog=prog, usage=usage, description=description, epilog=epilog)

    def add_arguments(self, optional, arg_type, action='store', nargs=1, const=None, default=argparse.SUPPRESS, choices=None, required=False,
                      arg_help_message=argparse.SUPPRESS, metavar=argparse.SUPPRESS, dest=None):
        """
        Adds a custom argument depending on desired options
        :param optional: Either a name or a list of option strings, e.g. foo or -f, --foo.
        :param arg_type: The type to which the command-line argument should be converted.
        :param action: The basic type of action to be taken when this argument is encountered at the command line.
        :param nargs: The number of command-line arguments that should be consumed.
        :param const: A constant value required by some action and nargs selections.
        :param default: The value produced if the argument is absent from the command line and if it is absent from the namespace object.
        :param choices: A container of the allowable values for the argument.
        :param required: Whether the command-line option may be omitted (optionals only).
        :param arg_help_message: A brief description of what the argument does.
        :param metavar: A name for the argument in usage messages.
        :param dest: The name of the attribute to be added to the object returned by parse_args().
        :return:
        """
        self.parser.add_argument(optional[0],
                                 optional[1],
                                 action=action,
                                 nargs=nargs,
                                 const=const,
                                 default=default,
                                 type=arg_type,
                                 choices=choices,
                                 required=required,
                                 help=arg_help_message,
                                 metavar=metavar,
                                 dest=dest)

    def parse_arguments(self):
        """
        Parses all added arguments
        :return: returns all parsed arguments
        """
        return self.parser.parse_args()
