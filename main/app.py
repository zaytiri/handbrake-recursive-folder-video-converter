import sys

from configure_arguments import ConfigureArguments
from search import Search

# .\HandBrakeCLI.exe --preset "Very Fast 1080p30" -i
# .\advanced-python\01-Introduction\01-Welcome.mp4 -o
# .\advanced-python\01-Introduction\01-Welcome.mkv

arguments = ConfigureArguments().configure_arguments()

folder_path = arguments.convert.value
original_file_extension = arguments.extensions.value
target_file_extension = arguments.target.value
to_delete_folder_name = arguments.delete_folder.value

response = input('"' + folder_path + '" is going to be modified permanently. Are you sure you want to continue? \n [Y/N]')

if response == 'N':
    sys.exit()
elif response == 'Y':
    print('All files found with the a ', end="")

    first = True
    for extension in original_file_extension:
        if first:
            print(extension, end="")
            first = False
            continue

        print(' or ' + extension, end="")

    print(' extension are going to be converted to ' + target_file_extension + ' extension and be kept in the "' + to_delete_folder_name + '" '
                                                                                                                                           'folder.\n')

    videos = Search(arguments.root.value, arguments.convert.value, arguments.extensions.value, arguments.target.value, arguments.delete_folder.value)
    videos.search()
