import os

from havc.entities.command_arguments import CommandArguments
from .configuration_line import ConfigurationLine, MultipleConfigurationLine, InitialDotLine
from havc.services.directory import Directory
from havc.services.file import File


class Configurations:
    original_arguments = None
    arguments = CommandArguments()
    current_configurations = []
    path = os.path.dirname(os.path.realpath(__file__)) + '\\config.txt'
    file = File(path)

    def set_original_arguments(self, original_arguments):
        self.original_arguments = original_arguments

    def process(self):
        self.__configure()
        return self.__get_configurations()

    def is_configured(self):
        directory = Directory(self.file.path)
        if not directory.exists():
            return False

        if self.file.is_empty():
            return False
        return True

    @staticmethod
    def __get_current_configuration(line):
        return line.split('==')[1]

    def __process_configuration(self, configuration):

        if configuration.name not in self.original_arguments:
            try:
                self.file.set_lines()
            except FileNotFoundError:
                return ""

            try:
                configuration.set_configuration(self.__get_current_configuration(self.file.get_lines()[configuration.index]).strip('\n'))
            except IndexError:
                pass
        else:
            new_argument_value = getattr(self.original_arguments, configuration.name)
            if len(new_argument_value) == 1:
                new_argument_value = new_argument_value[0]

            configuration.set_configuration(new_argument_value)

            # todo: refactor the following line of code to not check for specific instances. see patterns.
            if isinstance(configuration, MultipleConfigurationLine) or isinstance(configuration, InitialDotLine):
                configuration.add_initial_dot()

        self.current_configurations.append(configuration)
        return configuration.get_formatted()

    def __configure(self):
        """
        creates a new file and writes all mandatory arguments
        """
        new_file = ''

        arguments = self.arguments.to_list()

        index = 0
        for configuration in arguments:
            # todo: refactor the following lines of code to not check for specific instances. see design patterns.
            if configuration.name == self.arguments.original_extensions.name:
                new_config = MultipleConfigurationLine(configuration.name, index)
            elif configuration.name == self.arguments.target_extension.name:
                new_config = InitialDotLine(configuration.name, index)
            else:
                new_config = ConfigurationLine(configuration.name, index)
            new_file += self.__process_configuration(new_config)
            index += 1

        self.file.write_lines(new_file, 'w')

    def __get_configurations(self):
        """
        gets all argument values saved in the configuration file and returns them for easy access by the havc program
        :return: all argument values either from the configuration file or the command line
        """
        arguments = self.arguments.to_list()
        index = 0
        for configuration in arguments:
            try:
                configuration.set_argument_value(self.current_configurations[index].configuration)
                index += 1
            except IndexError:
                continue

        self.arguments.from_list(arguments)

        return self.arguments
