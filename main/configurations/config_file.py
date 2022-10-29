from main.entities.command_arguments import CommandArguments
from .configuration_line import ConfigurationLine, OriginalExtensionsLine, TargetLine
from main.services.directory import Directory


class ConfigurationFile:
    configuration_file_path = 'configurations\\config.txt'
    original_arguments = None
    arguments = CommandArguments()
    file_configurations = []
    current_file_lines = []

    def set_original_arguments(self, original_arguments):
        self.original_arguments = original_arguments

    def process(self):
        self.__create()

        return self.__get_configurations()

    def is_configured(self):
        directory = Directory(self.configuration_file_path)
        if directory.exists() and len(self.__get_lines()) != 0:
            return True
        return False

    @staticmethod
    def __get_current_configuration(line):
        return line.split('==')[1]

    def __write(self, lines):
        opened_config_file = open(self.configuration_file_path, 'w')
        opened_config_file.writelines(lines)
        opened_config_file.close()

    def __get_lines(self):
        return open(self.configuration_file_path).readlines()

    def __process_configuration_line(self, configuration_line):

        if configuration_line.name not in self.original_arguments:
            configuration_line.set_configuration(self.__get_current_configuration(self.current_file_lines[configuration_line.index]).strip('\n'))
        else:
            new_argument_value = getattr(self.original_arguments, configuration_line.name)
            if len(new_argument_value) == 1:
                new_argument_value = new_argument_value[0]

            configuration_line.set_configuration(new_argument_value)

            if isinstance(configuration_line, OriginalExtensionsLine) or isinstance(configuration_line, TargetLine):
                configuration_line.add_initial_dot()

        self.file_configurations.append(configuration_line)
        return configuration_line.get_formatted()

    def __create(self):
        """
        creates a new file and writes all mandatory arguments
        """
        if self.is_configured():
            self.current_file_lines = self.__get_lines()

        new_file = ''

        root_configuration = ConfigurationLine(self.arguments.root.name, 0)
        new_file += self.__process_configuration_line(root_configuration)

        path_to_convert_configuration = ConfigurationLine(self.arguments.folder_path_to_convert.name, 1)
        new_file += self.__process_configuration_line(path_to_convert_configuration)

        extensions_configuration = OriginalExtensionsLine(self.arguments.original_extensions.name, 2)
        new_file += self.__process_configuration_line(extensions_configuration)

        target_extension_configuration = TargetLine(self.arguments.target_extension.name, 3)
        new_file += self.__process_configuration_line(target_extension_configuration)

        self.__write(new_file)

    def __get_configurations(self):
        """
        gets all argument values saved in the configuration file and returns them for easy access by the main program
        :return: all argument values either from the configuration file or the command line
        """
        self.arguments.root.set_argument_value(self.file_configurations[0].configuration)
        self.arguments.folder_path_to_convert.set_argument_value(self.file_configurations[1].configuration)

        self.arguments.original_extensions.set_argument_value(self.file_configurations[2].configuration)

        self.arguments.target_extension.set_argument_value(self.file_configurations[3].configuration)
        self.arguments.deleted_folder.set_argument_value(self.original_arguments.delete_folder)

        return self.arguments
