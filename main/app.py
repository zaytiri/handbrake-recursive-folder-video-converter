import sys

from configure_arguments import ConfigureArguments
from search import Search

# .\HandBrakeCLI.exe --preset "Very Fast 1080p30" -i
# .\advanced-python\01-Introduction\01-Welcome.mp4 -o
# .\advanced-python\01-Introduction\01-Welcome.mkv

arguments = ConfigureArguments().configure_arguments()

response = input('"' + arguments.folderPathToConvert.value + '" is going to be modified permanently. Are you sure you want to continue? \n [Y/N]')

if response == 'N':
    sys.exit()
elif response == 'Y':
    print('All files found with the a ', end="")

    first = True
    for extension in arguments.originalExtensions.value:
        if first:
            print(extension, end="")
            first = False
            continue

        print(' or ' + extension, end="")

    print(' extension are going to be converted to ' + arguments.targetExtension.value + ' extension and be kept in the "' + arguments.deletedFolder.value + '" '
                                                                                                                                           'folder.\n')

    videos = Search(arguments)
    videos.search()
