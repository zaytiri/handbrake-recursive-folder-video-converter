class File:
    file_in_use = None

    def __init__(self, file_path):
        self.__file_path = file_path

    def open(self, mode):
        self.file_in_use = open(self.__file_path, mode)

    def close(self):
        self.file_in_use.close()

    def write(self, line):
        self.file_in_use.write(line)

    def write_lines(self, lines, mode):
        opened_config_file = open(self.__file_path, mode)
        opened_config_file.writelines(lines)
        opened_config_file.close()

    def get_lines(self):
        return open(self.__file_path).readlines()
