import os
import shutil
import subprocess
import sys

from entities.file_info import FileInfo


class Search:
    def __init__(self, arguments):
        self.folderPath = arguments.folderPathToConvert.value
        self.rootPath = arguments.root.value
        self.originalFileExtensions = arguments.originalExtensions.value
        self.targetFileExtension = arguments.targetExtension.value
        self.toDeleteFolderName = arguments.deletedFolder.value

    def search(self):
        for root, dirs, files in os.walk(self.folderPath):
            if self.toDeleteFolderName in root:
                continue

            for video in files:
                fileInfo = FileInfo(video, self.folderPath, self.originalFileExtensions)
                fileInfo.process_file()

                if fileInfo.isToConvert:
                    print('Current file being converted: ' + video)

                    command = '.\\HandBrakeCLI.exe --preset "Very Fast 1080p30" -i "{}'.format(fileInfo.fileAbsolutePath) + \
                              fileInfo.extension + '" -o "{}'.format(fileInfo.fileAbsolutePath) + \
                              self.targetFileExtension + '"'

                    print('Current Command: ' + command + '\n')

                    s = subprocess.run(command, shell=True, cwd=self.rootPath)
                    print(s)

                    path_name_splitted = root.split('\\')
                    parent_folder = path_name_splitted[len(path_name_splitted) - 1]

                    # print(path_name_splitted)
                    # print(parent_folder)

                    # create a folder to keep files already encoded and to be deleted later
                    to_delete_folder = ''
                    for folder in path_name_splitted:
                        if folder != parent_folder:
                            to_delete_folder = to_delete_folder + folder + '\\'

                    to_delete_folder = to_delete_folder + self.toDeleteFolderName
                    if not os.path.isdir(to_delete_folder):
                        os.mkdir(to_delete_folder)

                    # copy original mp4 file to a folder to be deleted later and remove said file from original location
                    original = r'{}'.format(fileInfo.fileAbsolutePath) + fileInfo.extension

                    new_folder = to_delete_folder + '\\' + parent_folder
                    if not os.path.isdir(new_folder):
                        os.mkdir(new_folder)

                    target = r'{}\{}'.format(new_folder, fileInfo.fileNameOnly + fileInfo.extension)

                    print(target)

                    shutil.copyfile(original, target)

                    os.remove(fileInfo.fileAbsolutePath + fileInfo.extension)
