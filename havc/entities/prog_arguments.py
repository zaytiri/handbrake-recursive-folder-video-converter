import textwrap

from .argument import Argument, Extensions


class ProgArguments:
    """
    This class is responsible for creating an object containing all arguments used in the program
    """

    def __init__(self):
        self.root = Argument('root',
                             '-r',
                             '--root',
                             'absolute path to the following file: HandBrakeCLI.exe. example: --root \'C:\\path\\to\\folder\'',
                             "")

        self.folder_path_to_convert = Argument('convert',
                                               '-c',
                                               '--convert',
                                               'absolute path to the folder with convertible videos. example: --convert \'C:\\path\\to\\folder\'',
                                               "")

        self.original_extensions = Extensions('extensions',
                                              '-e',
                                              '--extensions',
                                              'list of video\'s extensions to find and convert (with or without \'.\'). example: --extensions .mp4 '
                                              'm4v',
                                              "")

        self.target_extension = Extensions('target',
                                           '-t',
                                           '--target',
                                           'a target video extension to apply when a video is converted',
                                           "")

        self.deleted_folder = Argument('delete_folder',
                                       '-d',
                                       '--delete-folder',
                                       'name of the folder containing original files. default is: \'TO-DELETE\'',
                                       "",
                                       default='TO-DELETE')

        self.custom_command = Argument('custom_command',
                                       '-cc',
                                       '--custom-command',
                                       textwrap.dedent('''\
                                       a custom command inserted by the user. placeholders must be used for the original file and the converted 
                                       file. this command is supposed to work dynamically for a list of files searched in a folder, so:\n'
                                       'example: "--preset "Very Fast 1080p30" -i {of} -o {cf}"\n'
                                       '{of} => original file\n'
                                       '{cf} => converted file\n'
                                       'strings in the command must be between single quotes ->\'\'<-\n'
                                       'if the user wants to no longer use the custom command saved in the configs, the following can be inputted 
                                       instead: -cc OFF'''),
                                       "",
                                       default='OFF')

        self.safety_question = Argument('safety_question',
                                        '',
                                        '--safety-question',
                                        '[WARNING: make sure the folder to convert path is the correct one] enable/disable safety question '
                                        'regarding modifying files in path of folder to convert: (default is enabled)'
                                        'True: --safety-question | False: --no-safety-question',
                                        "",
                                        default=True)

        self.shutdown_when_done = Argument('shutdown',
                                           '',
                                           '--shutdown',
                                           'enable/disable if computer will be shutdown when the program is done: (default is disabled)'
                                           'True: --shutdown | False: --no-shutdown',
                                           "",
                                           default=False)

    def to_list(self):
        arguments = [
            self.root,
            self.folder_path_to_convert,
            self.original_extensions,
            self.target_extension,
            self.deleted_folder,
            self.custom_command,
            self.safety_question,
            self.shutdown_when_done
        ]
        return arguments

    def from_list(self, arguments):
        self.root = arguments[0]
        self.folder_path_to_convert = arguments[1]
        self.original_extensions = arguments[2]
        self.target_extension = arguments[3]
        self.deleted_folder = arguments[4]
        self.custom_command = arguments[5]
        self.safety_question = arguments[6]
        self.shutdown_when_done = arguments[7]
