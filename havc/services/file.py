class File:
    file_in_use = None
    __lines = []

    def __init__(self, path):
        self.path = path

    def open(self, mode):
        self.file_in_use = open(self.path, mode)

    def close(self):
        self.file_in_use.close()

    def write(self, line):
        self.file_in_use.write(line)

    def write_lines(self, lines, mode):
        opened_file = open(self.path, mode)
        opened_file.writelines(lines)
        opened_file.close()

    def set_lines(self):
        self.__lines = open(self.path).readlines()

    def get_lines(self):
        return self.__lines

    def is_empty(self):
        self.set_lines()
        return len(self.get_lines()) == 0
