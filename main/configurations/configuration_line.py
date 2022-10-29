class ConfigurationLine:
    configuration = ''

    def __init__(self, name, index):
        self.name = name
        self.index = index

    def get_formatted(self):
        if self.configuration == '':
            return ''

        return self.name + '==' + self.configuration + '\n'

    def set_configuration(self, configuration):
        self.configuration = configuration


class OriginalExtensionsLine(ConfigurationLine):
    def __init__(self, name, index):
        super().__init__(name, index)

    def add_initial_dot(self):
        for ext in self.configuration:
            if not ext.startswith('.'):
                self.configuration[self.configuration.index(ext)] = '.' + ext

    def set_configuration(self, configuration):
        self.configuration = configuration.split(',')

    def get_formatted(self):
        if self.configuration == '':
            return ''

        extensions = ''
        first = True

        for ext in self.configuration:
            if first:
                extensions += ext
                first = False
                continue

            extensions += ',' + ext

        return self.name + '==' + extensions + '\n'


class TargetLine(ConfigurationLine):

    def __init__(self, name, index):
        super().__init__(name, index)

    def add_initial_dot(self):
        new_target_line = ''

        if not self.configuration.startswith('.'):
            new_target_line += '.'
        new_target_line += self.configuration

        self.configuration = new_target_line
