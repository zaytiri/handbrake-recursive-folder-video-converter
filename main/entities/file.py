import shutil
import directory


class File:
    extension = ''
    absolutePath = ''
    nameOnly = ''

    def __init__(self, name, root, fileExtensionsToConvert):
        self.__name = name
        self.__root = root
        self.__fileExtensionsToConvert = fileExtensionsToConvert

    def process(self):
        """
        first checks if the file is to convert, and if not, returns False immediately without processing the rest.
        processes file to store the file name, the extension and its absolute path.
        :return: True if the file processes completely. False if the file is not to convert.
        """
        if not self.__process_extension_file():
            return False

        self.__process_file_name()
        self.__process_absolute_path()

        return True

    def copy_to(self, newPath):
        """
        copy original video file to a folder to be deleted later. removes said file from original location.
        :param newPath: new location for the video file
        """
        original = r'{}'.format(self.absolutePath) + self.extension
        target = directory.create_directory(newPath, self.nameOnly + self.extension)

        shutil.copyfile(original, target)

        directory.remove_directory(self.absolutePath + self.extension)

    def __process_file_name(self):
        fileName = self.__name.split('.')
        fileName.pop()
        self.nameOnly = '.'.join(fileName)

    def __process_extension_file(self):
        for ext in self.__fileExtensionsToConvert:
            if ext in self.__name:
                self.extension = ext
                return True
        return False

    def __process_absolute_path(self):
        self.absolutePath = directory.create_directory(self.__root, self.nameOnly)
