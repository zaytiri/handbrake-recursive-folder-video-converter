import sys

from services.arguments_service import ArgumentsService
from entities.command_arguments import CommandArguments
from configurations.configurations import Configurations
from utils.version import get_version


class ConfigureArguments:
    """
    This class is responsible for configuring all arguments required for the program to work including saving all mandatory argument values in a
    configuration file for easy frequent use. This way the user only has to configure the first time it runs the program or if the configuration
    file does not exist.
    """

    def __init__(self):
        self.args = None
        self.original_arguments = None
        self.arguments = CommandArguments()
        self.are_configs_saved = False

    def configure_arguments(self):
        """
        create and configure arguments to save in a configuration file
        :return: returns all arguments either from the command line or saved configuration file
        """

        self.args = ArgumentsService(prog="Handbrake Automatic Video Converter",
                                     usage="an automatic video converter/encoder using the HandBrake CLI",
                                     description="this program is meant to convert/encode video from various formats using the rules and syntax of "
                                                 "the HandBrake CLI. the following commands should explain the arguments.")

        config_file = Configurations()

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
        self.args.parser.add_argument('--version', action='version', version='%(prog)s ' + get_version())

        self.args.add_arguments([self.arguments.root.abbreviation_name, self.arguments.root.full_name],
                                str,
                                required=not self.are_configs_saved,
                                arg_help_message=self.arguments.root.help_message,
                                metavar=self.arguments.root.metavar)

        self.args.add_arguments([self.arguments.folder_path_to_convert.abbreviation_name, self.arguments.folder_path_to_convert.full_name],
                                str,
                                required=not self.are_configs_saved,
                                arg_help_message=self.arguments.folder_path_to_convert.help_message,
                                metavar=self.arguments.folder_path_to_convert.metavar)

        self.args.add_arguments([self.arguments.original_extensions.abbreviation_name, self.arguments.original_extensions.full_name],
                                str,
                                action='extend', nargs='+',
                                required=not self.are_configs_saved,
                                arg_help_message=self.arguments.original_extensions.help_message,
                                metavar=self.arguments.original_extensions.metavar)

        self.args.add_arguments([self.arguments.target_extension.abbreviation_name, self.arguments.target_extension.full_name],
                                str,
                                required=not self.are_configs_saved,
                                arg_help_message=self.arguments.target_extension.help_message,
                                metavar=self.arguments.target_extension.metavar)

        self.args.add_arguments([self.arguments.deleted_folder.abbreviation_name, self.arguments.deleted_folder.full_name],
                                str,
                                required=False,
                                arg_help_message=self.arguments.deleted_folder.help_message,
                                default=self.arguments.deleted_folder.default,
                                metavar=self.arguments.deleted_folder.metavar)

        self.args.add_arguments([self.arguments.custom_command.abbreviation_name, self.arguments.custom_command.full_name],
                                str,
                                required=False,
                                arg_help_message=self.arguments.custom_command.help_message,
                                default=self.arguments.custom_command.default,
                                metavar=self.arguments.custom_command.metavar)

    def __target_and_original_extensions_are_the_same(self):
        try:
            for ext in self.original_arguments.extensions:
                if ext in self.original_arguments.target[0]:
                    return True
            return False
        except AttributeError:
            return False
