import os.path
from os.path import exists


class Directory:
    current_folder = ''
    last_folder_path = ''

    def __init__(self, root):
        self.__root = root
        self.get_current_folder()
        self.get_last_directory()

    def get_last_directory(self):
        self.last_folder_path = os.path.dirname(self.__root)

    def get_current_folder(self):
        self.current_folder = os.path.basename(os.path.normpath(self.__root))

    def create(self, new_folder):
        return os.path.join(self.__root, new_folder)

    def create_folder(self, new_folder):
        new_directory = self.create(new_folder)
        if not os.path.isdir(new_directory):
            os.mkdir(new_directory)

        return new_directory

    def search_through(self):
        return os.walk(self.__root)

    def remove(self):
        os.remove(self.__root)

    def exists(self):
        return exists(self.__root)
