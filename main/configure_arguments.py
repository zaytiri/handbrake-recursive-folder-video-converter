from os.path import exists

from services.arguments_service import ArgumentsService
from entities.command_arguments import CommandArguments


class ConfigureArguments:
    """
    This class is responsible for configuring all arguments required for the program to work including saving all mandatory argument values in a
    configuration file for easy frequent use. This way the user only has to configure the first time it runs the program or if the configuration
    file does not exist.
    """
    fileName = 'config.txt'

    def __init__(self):
        self.args = ArgumentsService()  # configure name, description, etc
        self.areConfigsSaved = False
        self.originalArguments = None
        self.arguments = CommandArguments()

    def configure_arguments(self):
        """
        create and configure arguments to save in a configuration file
        :return: returns all arguments either from the command line or saved configuration file
        """
        if exists(self.fileName) and not len(open(self.fileName).readlines()) == 0:
            self.areConfigsSaved = True

        self.add_arguments()

        self.originalArguments = self.args.parse_arguments()

        if not self.areConfigsSaved:
            self.create_config_file()
            return self.get_config_file_entries()

        self.overwrite_config_file()
        return self.get_config_file_entries()

    def add_arguments(self):
        """
        configures and adds the arguments required for the program
        """
        self.args.add_arguments([self.arguments.root.abrName, self.arguments.root.fullName], str, required=not self.areConfigsSaved,
                                arg_help_message='absolute path to the following file: HandBrakeCLI.exe. '
                                                 'example: '
                                                 '--root \'C:\\path\\to\\folder\'')

        self.args.add_arguments([self.arguments.convert.abrName, self.arguments.convert.fullName], str, required=not self.areConfigsSaved,
                                arg_help_message='absolute path to the folder with convertible videos. example: '
                                                 '--convert \'C:\\path\\to\\folder\'')

        self.args.add_arguments([self.arguments.extensions.abrName, self.arguments.extensions.fullName], str, action='extend', nargs='+',
                                required=not self.areConfigsSaved,
                                arg_help_message='list of video\'s extensions to find and convert (with or without \'.\'). example: --extensions '
                                                 '.mp4 m4v')

        self.args.add_arguments([self.arguments.target.abrName, self.arguments.target.fullName], str, required=not self.areConfigsSaved,
                                arg_help_message='a target video extension to apply when a video is converted')

        self.args.add_arguments([self.arguments.delete_folder.abrName, self.arguments.delete_folder.fullName], str, required=False,
                                arg_help_message='name of the folder containing original files. default is: \'TO-DELETE\'', default='TO-DELETE')

    def create_config_file(self):
        """
        creates a new file and writes all mandatory arguments
        """
        configFile = open(self.fileName, 'w')
        configFile.write(self.arguments.root.name + '==' + self.originalArguments.root[0] + '\n')
        configFile.write(self.arguments.convert.name + '==' + self.originalArguments.convert[0] + '\n')

        configFile.write(self.arguments.extensions.name + '==')
        for ext in self.originalArguments.extensions:
            configFile.write(ext + ',')
        configFile.write('\n')

        configFile.write(self.arguments.target.name + '==' + self.originalArguments.target[0])
        configFile.close()

    def overwrite_config_file(self):
        """
        checks whether the argument value must be replaced in the configuration file
        """
        lines = open(self.fileName).readlines()
        configFile = open(self.fileName, 'w')
        try:
            if not self.originalArguments.root[0] == lines[0].split('==')[1]:
                lines[0] = 'root==' + self.originalArguments.root[0] + '\n'
        except AttributeError:
            pass

        try:
            if not self.originalArguments.convert[0] == lines[1].split('==')[1]:
                lines[1] = 'convert==' + self.originalArguments.convert[0] + '\n'
        except AttributeError:
            pass

        try:
            if self.originalArguments.extensions:
                pass
            lines[2] = 'extensions=='
            for ext in self.originalArguments.extensions:
                lines[2] += ext + ','
            lines[2] += '\n'
        except AttributeError:
            pass

        try:
            if not self.originalArguments.target[0] == lines[3].split('==')[1]:
                lines[3] = 'target==' + self.originalArguments.target[0]
        except AttributeError:
            pass

        configFile.writelines(lines)
        configFile.close()

    def get_config_file_entries(self):
        """
        gets all argument values saved in the configuration file and returns them for easy access by the main program
        :return: all argument values either from the configuration file or the command line
        """
        lines = open(self.fileName).readlines()

        self.arguments.root.set_argument_value(lines[0].split('==')[1].strip('\n'))
        self.arguments.convert.set_argument_value(lines[1].split('==')[1].strip('\n'))

        extensions = lines[2].split('==')[1].split(',')
        extensions.pop()
        for ext in extensions:
            if not ext.startswith('.'):
                extensions[extensions.index(ext)] = '.' + ext
        self.arguments.extensions.set_argument_value(extensions)

        self.arguments.target.set_argument_value(lines[3].split('==')[1].strip('\n'))
        self.arguments.delete_folder.set_argument_value(self.originalArguments.delete_folder)

        return self.arguments
