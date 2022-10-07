import subprocess
import sys
import os
import argparse
import shutil

root_path = 'C:\\Users\\ziia\\Desktop' # location of the following program: HandBrakeCLI.exe
# folder_path = 'C:\\Users\\ziia\\Desktop\\advanced-python'

# .\HandBrakeCLI.exe --preset "Very Fast 1080p30" -i
# .\advanced-python\01-Introduction\01-Welcome.mp4 -o
# .\advanced-python\01-Introduction\01-Welcome.mkv

try:
    folder_path = sys.argv[1]
    original_file_extension = '.' + sys.argv[2]
    target_file_extension = '.' + sys.argv[3]
    to_delete_folder_name = 'TO-DELETE'

    response = input(sys.argv[1] + ' is going to be modified permanently. Are you sure you want to continue? \n [Y/N]')

    if response == 'N':
        sys.exit()
    elif response == 'Y':
        print('All files found with the a ' + original_file_extension + ' extension are going to be converted to ' + target_file_extension +
              ' extension and be kept in the "TO-DELETE" folder\n')
        for root, dirs, files in os.walk(folder_path):
            # print('root: ' + str(root))
            # print('dirs: ' + str(dirs))
            # print('files: ' + str(files))

            if to_delete_folder_name in root:
                continue

            for mp4_file in files:
                if original_file_extension in mp4_file:
                    print('Current file being converted: ' + mp4_file)

                    file_path = root + '\\' + mp4_file.split('.')[0]
                    command = '.\\HandBrakeCLI.exe --preset "Very Fast 1080p30" -i "{}'.format(file_path) + \
                              original_file_extension + '" -o "{}'.format(file_path) + \
                              target_file_extension + '"'

                    # print(file_path)
                    print('Current Command: ' + command + '\n')
                    s = subprocess.run(command, shell=True, cwd=root_path)
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

                    to_delete_folder = to_delete_folder + to_delete_folder_name
                    if not os.path.isdir(to_delete_folder):
                        os.mkdir(to_delete_folder)

                    # copy original mp4 file to a folder to be deleted later and remove said file from original location
                    original = r'{}'.format(file_path) + original_file_extension

                    new_folder = to_delete_folder + '\\' + parent_folder
                    if not os.path.isdir(new_folder):
                        os.mkdir(new_folder)

                    target = r'{}\{}'.format(new_folder, mp4_file)

                    shutil.copyfile(original, target)

                    os.remove(file_path + original_file_extension)
except IndexError:
    print('missing arguments')
    sys.exit()
