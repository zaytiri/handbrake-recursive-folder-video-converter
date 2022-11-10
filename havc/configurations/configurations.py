import os

import yaml

from havc.entities.prog_arguments import ProgArguments
from havc.services.directory import Directory
from havc.services.file import File


class Configurations:
    original_arguments = None
    arguments = ProgArguments()
    settings = {}
    path = os.path.dirname(os.path.realpath(__file__)) + '\\userconfigs.yaml'
    file = File(path)

    def set_original_arguments(self, original_arguments):
        self.original_arguments = original_arguments

    def process(self):
        if self.is_configured():
            configs_file = self.file.open('r')
            self.settings = yaml.safe_load(configs_file)
            self.file.close()

        self.__configure()

        return self.arguments

    def is_configured(self):
        directory = Directory(self.file.path)
        if not directory.exists():
            return False

        if self.file.is_empty():
            return False
        return True

    def __configure(self):
        """
        creates a new file and writes all mandatory arguments
        """
        arguments = self.arguments.to_list()

        for configuration in arguments:
            self.settings[configuration.name] = self.__process_configuration(configuration)

        configs_file = self.file.open('w')
        yaml.safe_dump(self.settings, configs_file)
        self.file.close()

        self.arguments.from_list(arguments)

    def __process_configuration(self, configuration):
        if configuration.name not in self.original_arguments:
            if not self.is_configured():
                argument_value = configuration.default
            else:
                try:
                    argument_value = self.settings[configuration.name]
                except KeyError:
                    argument_value = configuration.default
        else:
            argument_value = getattr(self.original_arguments, configuration.name)

        configuration.set_argument_value(argument_value)
        return configuration.value
