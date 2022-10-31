from .argument import Argument


class CommandArguments:
    """
    This class is responsible for creating an object containing all arguments used in the program
    """

    def __init__(self):
        self.root = Argument('root', '-r', '--root')
        self.folder_path_to_convert = Argument('convert', '-c', '--convert')
        self.original_extensions = Argument('extensions', '-e', '--extensions')
        self.target_extension = Argument('target', '-t', '--target')
        self.deleted_folder = Argument('delete_folder', '-d', '--delete-folder')

    def to_list(self):
        arguments = [
            self.root,
            self.folder_path_to_convert,
            self.original_extensions,
            self.target_extension,
            self.deleted_folder
        ]
        return arguments

    def from_list(self, arguments):
        self.root = arguments[0]
        self.folder_path_to_convert = arguments[1]
        self.original_extensions = arguments[2]
        self.target_extension = arguments[3]
        self.deleted_folder = arguments[4]
