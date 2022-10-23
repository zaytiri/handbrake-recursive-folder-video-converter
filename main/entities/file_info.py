
class FileInfo:
    extension = ''
    isToConvert = False
    fileAbsolutePath = ''
    fileNameOnly = ''

    def __init__(self, name, root, fileExtensionsToConvert):
        self.__name = name
        self.__root = root
        self.__fileExtensionsToConvert = fileExtensionsToConvert

    def process_file(self):
        self.__process_file_name()
        self.__process_extension_file()
        self.__process_absolute_path()

    def __process_file_name(self):
        fileName = self.__name.split('.')
        fileName.pop()
        self.fileNameOnly = '.'.join(fileName)

    def __process_extension_file(self):
        for ext in self.__fileExtensionsToConvert:
            if ext in self.__name:
                self.extension = ext
                self.isToConvert = True
                return

    def __process_absolute_path(self):
        self.fileAbsolutePath = self.__root + "\\" + self.fileNameOnly

