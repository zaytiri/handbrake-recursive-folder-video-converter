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
        self.original_arguments = None
        self.arguments = CommandArguments()
        self.are_configs_saved = False

    def configure_arguments(self):
        """
        create and configure arguments to save in a configuration file
        :return: returns all arguments either from the command line or saved configuration file
        """

        config_file = ConfigurationFile()

        self.are_configs_saved = config_file.is_configured()

        self.__add_arguments()

        self.original_arguments = self.args.parse_arguments()

        if self.__target_and_original_extensions_are_the_same():
            print('ERROR: target extension cannot be the same as any of the original file extensions.')
            sys.exit()

        config_file.set_original_arguments(self.original_arguments)

        return config_file.process()

    def __add_arguments(self):
        """
        configures and adds the arguments required for the program
        """
        self.args.add_arguments([self.arguments.root.abbreviation_name, self.arguments.root.fullName], str, required=not self.are_configs_saved,
                                arg_help_message='absolute path to the following file: HandBrakeCLI.exe. '
                                                 'example: '
                                                 '--root \'C:\\path\\to\\folder\'')

        self.args.add_arguments([self.arguments.folder_path_to_convert.abbreviation_name, self.arguments.folder_path_to_convert.full_name], str, required=not self.are_configs_saved,
                                arg_help_message='absolute path to the folder with convertible videos. example: '
                                                 '--convert \'C:\\path\\to\\folder\'')

        self.args.add_arguments([self.arguments.original_extensions.abbreviation_name, self.arguments.original_extensions.full_name], str, action='extend', nargs='+',
                                required=not self.are_configs_saved,
                                arg_help_message='list of video\'s extensions to find and convert (with or without \'.\'). example: --extensions '
                                                 '.mp4 m4v')

        self.args.add_arguments([self.arguments.target_extension.abbreviation_name, self.arguments.target_extension.full_name], str, required=not self.are_configs_saved,
                                arg_help_message='a target video extension to apply when a video is converted')

        self.args.add_arguments([self.arguments.deleted_folder.abbreviation_name, self.arguments.deleted_folder.full_name], str, required=False,
                                arg_help_message='name of the folder containing original files. default is: \'TO-DELETE\'', default='TO-DELETE')

    def __target_and_original_extensions_are_the_same(self):
        try:
            for ext in self.original_arguments.extensions:
                if ext in self.original_arguments.target[0]:
                    return True
            return False
        except AttributeError:
            return False

