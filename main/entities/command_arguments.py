from .argument import Argument


class CommandArguments:
    """
    This class is responsible for creating an object containing all arguments used in the program
    """
    def __init__(self):
        self.root = Argument('root', '-r', '--root')
        self.folderPathToConvert = Argument('convert', '-c', '--convert')
        self.originalExtensions = Argument('extensions', '-e', '--extensions')
        self.targetExtension = Argument('target', '-t', '--target')
        self.deletedFolder = Argument('delete_folder', '-d', '--delete-folder')
