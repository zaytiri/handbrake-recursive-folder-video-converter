from entities.file import File
from entities.directory import Directory
from command import Command


class Search:
    def __init__(self, arguments):
        self.folderPath = arguments.folderPathToConvert.value
        self.rootPath = arguments.root.value
        self.originalFileExtensions = arguments.originalExtensions.value
        self.targetFileExtension = arguments.targetExtension.value
        self.toDeleteFolderName = arguments.deletedFolder.value

    def search(self):
        mainDirectory = Directory(self.folderPath)
        for root, dirs, files in mainDirectory.search_through():
            if self.toDeleteFolderName in root:
                continue

            for video in files:
                file = File(video, self.folderPath, self.originalFileExtensions)

                if file.process():
                    print('Current file being converted: ' + file.nameOnly)

                    handbrake = Command(self.rootPath)
                    handbrake.run_command(file, self.targetFileExtension)

                    rootDirectory = Directory(root)
                    newDeleteDirectory = Directory(rootDirectory.lastFolderPath)
                    toDeleteFolderPath = newDeleteDirectory.create_folder(self.toDeleteFolderName)
                    newDeletedFolderDirectory = Directory(toDeleteFolderPath)
                    newDeletedFolderPath = newDeletedFolderDirectory.create_folder(rootDirectory.currentFolder)

                    file.copy_to(newDeletedFolderPath)
