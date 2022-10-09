import sys

from configure_arguments import ConfigureArguments
from search import Search

root_path = 'C:\\Users\\ziia\\Desktop' # location of the following program: HandBrakeCLI.exe
# folder_path = 'C:\\Users\\ziia\\Desktop\\advanced-python'

# .\HandBrakeCLI.exe --preset "Very Fast 1080p30" -i
# .\advanced-python\01-Introduction\01-Welcome.mp4 -o
# .\advanced-python\01-Introduction\01-Welcome.mkv

arguments = ConfigureArguments().configure_arguments()

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

        videos = Search(arguments.root.value, arguments.convert.value, arguments.extensions.value, arguments.target.value, arguments.delete_folder.value)
        videos.search()

except IndexError:
    print('missing arguments')
    sys.exit()
