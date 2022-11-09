from havc.services.directory import Directory
from havc.utils.error import throw
from .services.arguments_service import ArgumentsService
from .entities.prog_arguments import ProgArguments
from .configurations.configurations import Configurations
from .utils.progsettings import get_version


class Arguments:
    """
    This class is responsible for configuring all arguments required for the program to work including saving all mandatory argument values in a
    configuration file for easy frequent use. This way the user only has to configure the first time it runs the program or if the configuration
    file does not exist.
    """

    def __init__(self):
        self.args = None
        self.original_arguments = None
        self.prog_arguments = ProgArguments()
        self.are_configs_saved = False

    def configure(self):
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

        self.__check_any_errors()

        config_file.set_original_arguments(self.original_arguments)

        return config_file.process()

    def __add_arguments(self):
        """
        configures and adds the arguments required for the program
        """
        self.args.parser.add_argument('--version', action='version', version='%(prog)s ' + get_version())

        self.args.add_arguments([self.prog_arguments.root.abbreviation_name, self.prog_arguments.root.full_name],
                                str,
                                required=not self.are_configs_saved,
                                arg_help_message=self.prog_arguments.root.help_message,
                                metavar=self.prog_arguments.root.metavar)

        self.args.add_arguments([self.prog_arguments.folder_path_to_convert.abbreviation_name, self.prog_arguments.folder_path_to_convert.full_name],
                                str,
                                required=not self.are_configs_saved,
                                arg_help_message=self.prog_arguments.folder_path_to_convert.help_message,
                                metavar=self.prog_arguments.folder_path_to_convert.metavar)

        self.args.add_arguments([self.prog_arguments.original_extensions.abbreviation_name, self.prog_arguments.original_extensions.full_name],
                                str,
                                action='extend', nargs='+',
                                required=not self.are_configs_saved,
                                arg_help_message=self.prog_arguments.original_extensions.help_message,
                                metavar=self.prog_arguments.original_extensions.metavar)

        self.args.add_arguments([self.prog_arguments.target_extension.abbreviation_name, self.prog_arguments.target_extension.full_name],
                                str,
                                required=not self.are_configs_saved,
                                arg_help_message=self.prog_arguments.target_extension.help_message,
                                metavar=self.prog_arguments.target_extension.metavar)

        self.args.add_arguments([self.prog_arguments.deleted_folder.abbreviation_name, self.prog_arguments.deleted_folder.full_name],
                                str,
                                required=False,
                                arg_help_message=self.prog_arguments.deleted_folder.help_message,
                                default=self.prog_arguments.deleted_folder.default,
                                metavar=self.prog_arguments.deleted_folder.metavar)

        self.args.add_arguments([self.prog_arguments.custom_command.abbreviation_name, self.prog_arguments.custom_command.full_name],
                                str,
                                required=False,
                                arg_help_message=self.prog_arguments.custom_command.help_message,
                                default=self.prog_arguments.custom_command.default,
                                metavar=self.prog_arguments.custom_command.metavar)

    def __check_any_errors(self):
        if self.__target_and_original_extensions_are_the_same():
            throw('target extension cannot be the same as any of the original file extensions.')

        try:
            if not self.__given_argument_path_exists(self.original_arguments.root[0]):
                throw(self.original_arguments.root[0] + '\' path does not exist.')

            if not self.__given_argument_path_exists(self.original_arguments.convert[0]):
                throw(self.original_arguments.convert[0] + '\' path does not exist.')
        except AttributeError:
            pass

    def __target_and_original_extensions_are_the_same(self):
        try:
            for ext in self.original_arguments.extensions:
                if ext in self.original_arguments.target[0]:
                    return True
            return False
        except AttributeError:
            return False

    @staticmethod
    def __given_argument_path_exists(path):
        argument_path = Directory(path)
        return argument_path.exists()
