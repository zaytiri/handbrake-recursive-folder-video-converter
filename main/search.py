import os
import shutil
import subprocess


class Search:
    def __init__(self, root_path, folder_path, original_file_extensions, target_file_extension, to_delete_folder_name):
        self.folderPath = folder_path
        self.rootPath = root_path
        self.originalFileExtensions = original_file_extensions
        self.targetFileExtension = target_file_extension
        self.toDeleteFolderName = to_delete_folder_name

    def video_file_has_desired_extension(self, filename):
        for ext in self.originalFileExtensions:
            if ext in filename:
                return True
        return False

    def search(self):
        for root, dirs, files in os.walk(self.folderPath):
            # print('root: ' + str(root))
            # print('dirs: ' + str(dirs))
            # print('files: ' + str(files))

            if self.toDeleteFolderName in root:
                continue

            for video in files:
                if self.video_file_has_desired_extension(video):
                    print('Current file being converted: ' + video)

                    file_path = root + '\\' + video.split('.')[0]
                    current_extension = video.split('.')[1]
                    command = '.\\HandBrakeCLI.exe --preset "Very Fast 1080p30" -i "{}'.format(file_path) + \
                              self.originalFileExtensions + '" -o "{}'.format(file_path) + \
                              self.targetFileExtension + '"'

                    # print(file_path)
                    print('Current Command: ' + command + '\n')
                    s = subprocess.run(command, shell=True, cwd=self.rootPath)
                    # print(s)

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
                    original = r'{}'.format(file_path) + self.originalFileExtensions

                    new_folder = to_delete_folder + '\\' + parent_folder
                    if not os.path.isdir(new_folder):
                        os.mkdir(new_folder)

                    target = r'{}\{}'.format(new_folder, video)

                    shutil.copyfile(original, target)

                    os.remove(file_path + self.originalFileExtensions)