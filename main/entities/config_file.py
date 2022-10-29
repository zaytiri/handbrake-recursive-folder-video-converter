from .command_arguments import CommandArguments
from .configuration_line import ConfigurationLine, OriginalExtensionsLine, TargetLine
from .directory import Directory


class ConfigurationFile:
    name = 'config.txt'
    originalArguments = None
    arguments = CommandArguments()
    fileConfigurations = []
    currentFileLines = []

    def __init__(self):
        pass

    def set_original_arguments(self, originalArguments):
        self.originalArguments = originalArguments

    def process(self):
        self.__create()

        return self.__get_configurations()

    def is_configured(self):
        directory = Directory(self.name)
        if directory.exists() and not len(self.__get_lines()) == 0:
            return True
        return False

    @staticmethod
    def __get_current_configuration(line):
        return line.split('==')[1]

    def __write(self, lines):
        openedConfigFile = open(self.name, 'w')
        openedConfigFile.writelines(lines)
        openedConfigFile.close()

    def __get_lines(self):
        return open(self.name).readlines()

    def __process_configuration_line(self, configurationLine):

        if configurationLine.name not in self.originalArguments:
            configurationLine.set_configuration(self.__get_current_configuration(self.currentFileLines[configurationLine.index]).strip('\n'))
        else:
            newArgumentValue = getattr(self.originalArguments, configurationLine.name)
            if len(newArgumentValue) == 1:
                newArgumentValue = newArgumentValue[0]

            configurationLine.set_configuration(newArgumentValue)

            if isinstance(configurationLine, OriginalExtensionsLine) or isinstance(configurationLine, TargetLine):
                configurationLine.add_initial_dot()

        self.fileConfigurations.append(configurationLine)
        return configurationLine.get_formatted()

    def __create(self):
        """
        creates a new file and writes all mandatory arguments
        """
        if self.is_configured():
            self.currentFileLines = self.__get_lines()

        newFile = ''

        rootConfiguration = ConfigurationLine(self.arguments.root.name, 0)
        newFile += self.__process_configuration_line(rootConfiguration)

        pathToConvertConfiguration = ConfigurationLine(self.arguments.folderPathToConvert.name, 1)
        newFile += self.__process_configuration_line(pathToConvertConfiguration)

        extensionsConfiguration = OriginalExtensionsLine(self.arguments.originalExtensions.name, 2)
        newFile += self.__process_configuration_line(extensionsConfiguration)

        targetExtensionConfiguration = TargetLine(self.arguments.targetExtension.name, 3)
        newFile += self.__process_configuration_line(targetExtensionConfiguration)

        self.__write(newFile)

    def __get_configurations(self):
        """
        gets all argument values saved in the configuration file and returns them for easy access by the main program
        :return: all argument values either from the configuration file or the command line
        """
        self.arguments.root.set_argument_value(self.fileConfigurations[0].configuration)
        self.arguments.folderPathToConvert.set_argument_value(self.fileConfigurations[1].configuration)

        self.arguments.originalExtensions.set_argument_value(self.fileConfigurations[2].configuration)

        self.arguments.targetExtension.set_argument_value(self.fileConfigurations[3].configuration)
        self.arguments.deletedFolder.set_argument_value(self.originalArguments.delete_folder)

        return self.arguments
