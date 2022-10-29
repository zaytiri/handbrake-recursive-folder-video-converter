import sys
from os.path import exists

from services.arguments_service import ArgumentsService
from entities.command_arguments import CommandArguments
from entities.config_file import ConfigurationFile


class ConfigureArguments:
    """
    This class is responsible for configuring all arguments required for the program to work including saving all mandatory argument values in a
    configuration file for easy frequent use. This way the user only has to configure the first time it runs the program or if the configuration
    file does not exist.
    """

    def __init__(self):
        self.args = ArgumentsService()  # configure name, description, etc
        self.originalArguments = None
        self.arguments = CommandArguments()
        self.areConfigsSaved = False

    def configure_arguments(self):
        """
        create and configure arguments to save in a configuration file
        :return: returns all arguments either from the command line or saved configuration file
        """

        configFile = ConfigurationFile()

        self.areConfigsSaved = configFile.is_configured()

        self.__add_arguments()

        self.originalArguments = self.args.parse_arguments()

        if self.__target_and_original_extensions_are_the_same():
            print('ERROR: target extension cannot be the same as any of the original file extensions.')
            sys.exit()

        configFile.set_original_arguments(self.originalArguments)

        return configFile.process()

    def __add_arguments(self):
        """
        configures and adds the arguments required for the program
        """
        self.args.add_arguments([self.arguments.root.abrName, self.arguments.root.fullName], str, required=not self.areConfigsSaved,
                                arg_help_message='absolute path to the following file: HandBrakeCLI.exe. '
                                                 'example: '
                                                 '--root \'C:\\path\\to\\folder\'')

        self.args.add_arguments([self.arguments.folderPathToConvert.abrName, self.arguments.folderPathToConvert.fullName], str, required=not self.areConfigsSaved,
                                arg_help_message='absolute path to the folder with convertible videos. example: '
                                                 '--convert \'C:\\path\\to\\folder\'')

        self.args.add_arguments([self.arguments.originalExtensions.abrName, self.arguments.originalExtensions.fullName], str, action='extend', nargs='+',
                                required=not self.areConfigsSaved,
                                arg_help_message='list of video\'s extensions to find and convert (with or without \'.\'). example: --extensions '
                                                 '.mp4 m4v')

        self.args.add_arguments([self.arguments.targetExtension.abrName, self.arguments.targetExtension.fullName], str, required=not self.areConfigsSaved,
                                arg_help_message='a target video extension to apply when a video is converted')

        self.args.add_arguments([self.arguments.deletedFolder.abrName, self.arguments.deletedFolder.fullName], str, required=False,
                                arg_help_message='name of the folder containing original files. default is: \'TO-DELETE\'', default='TO-DELETE')

    def __target_and_original_extensions_are_the_same(self):
        try:
            for ext in self.originalArguments.extensions:
                if ext in self.originalArguments.target[0]:
                    return True
            return False
        except AttributeError:
            return False

