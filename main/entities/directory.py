import os.path
from os.path import exists


class Directory:
    currentFolder = ''
    lastFolderPath = ''

    def __init__(self, root):
        self.__root = root
        self.get_current_folder()
        self.get_last_directory()

    def get_last_directory(self):
        self.lastFolderPath = os.path.dirname(self.__root)

    def get_current_folder(self):
        self.currentFolder = os.path.basename(os.path.normpath(self.__root))

    def create(self, newFolder):
        return os.path.join(self.__root, newFolder)

    def create_folder(self, newFolder):
        newDirectory = self.create(newFolder)
        if not os.path.isdir(newDirectory):
            os.mkdir(newDirectory)

        return newDirectory

    def search_through(self):
        return os.walk(self.__root)

    def remove(self):
        os.remove(self.__root)

    def exists(self):
        return exists(self.__root)
