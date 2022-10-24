import os.path


def create_directory(path, newFolder):
    return os.path.join(path, newFolder)


def create_folder(path, newFolder):
    newDirectory = create_directory(path, newFolder)
    if not os.path.isdir(newDirectory):
        os.mkdir(newDirectory)

    return newDirectory


def search_through_directory(path):
    return os.walk(path)


def remove_directory(path):
    os.remove(path)


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
