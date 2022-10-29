import shutil
from .directory import Directory


class VideoFile:
    extension = ''
    absolute_path = ''
    name_only = ''

    def __init__(self, name, root, file_extensions_to_convert):
        self.__name = name
        self.__root = root
        self.__file_extensions_to_convert = file_extensions_to_convert

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

    def copy_to(self, new_path):
        """
        copy original video file to a folder to be deleted later. removes said file from original location.
        :param new_path: new location for the video file
        """
        directory = Directory(new_path)
        original = r'{}'.format(self.absolute_path) + self.extension
        target = directory.create(self.name_only + self.extension)

        shutil.copyfile(original, target)

        directory = Directory(self.absolute_path + self.extension)
        directory.remove()

    def __process_file_name(self):
        file_name = self.__name.split('.')
        file_name.pop()
        self.name_only = '.'.join(file_name)

    def __process_extension_file(self):
        for ext in self.__file_extensions_to_convert:
            if ext in self.__name:
                self.extension = ext
                return True
        return False

    def __process_absolute_path(self):
        directory = Directory(self.__root)
        self.absolute_path = directory.create(self.name_only)
