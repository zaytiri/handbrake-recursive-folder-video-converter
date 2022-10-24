from entities.file import File
import entities.directory as directory
from command import Command


class Search:
    def __init__(self, arguments):
        self.folderPath = arguments.folderPathToConvert.value
        self.rootPath = arguments.root.value
        self.originalFileExtensions = arguments.originalExtensions.value
        self.targetFileExtension = arguments.targetExtension.value
        self.toDeleteFolderName = arguments.deletedFolder.value

    def search(self):
        for root, dirs, files in directory.search_through_directory(self.folderPath):
            if self.toDeleteFolderName in root:
                continue

            for video in files:
                file = File(video, self.folderPath, self.originalFileExtensions)

                if file.process():
                    print('Current file being converted: ' + file.nameOnly)

                    # handbrake = Command(self.rootPath)
                    # handbrake.run_command(file, self.targetFileExtension)

                    rootDirectory = directory.Directory(root)
                    toDeleteFolderPath = directory.create_folder(rootDirectory.lastFolderPath, self.toDeleteFolderName)
                    newDeletedFolderPath = directory.create_folder(toDeleteFolderPath, rootDirectory.currentFolder)

                    # file.copy_to(newDeletedFolderPath)
