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
