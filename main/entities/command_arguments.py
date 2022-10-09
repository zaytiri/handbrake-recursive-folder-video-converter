from .argument import Argument


class CommandArguments:
    """
    This class is responsible for creating an object containing all arguments used in the program
    """
    def __init__(self):
        self.root = Argument('root', '-r', '--root')
        self.convert = Argument('convert', '-c', '--convert')
        self.extensions = Argument('extensions', '-e', '--extensions')
        self.target = Argument('target', '-t', '--target')
        self.delete_folder = Argument('delete_folder', '-d', '--delete-folder')
