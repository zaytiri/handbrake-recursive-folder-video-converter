import sys

from .arguments import Arguments
from .search import Search


def main():
    arguments = Arguments().configure()

    response = input(
        '"' + arguments.folder_path_to_convert.value + '" is going to be modified permanently. Are you sure you want to continue? \n [Y/N]')

    if response == 'N':
        sys.exit()
    elif response == 'Y':
        print('All files found with the a ', end="")

        first = True
        for extension in arguments.original_extensions.value:
            if first:
                print(extension, end="")
                first = False
                continue

            print(' or ' + extension, end="")

        print(
            ' extension are going to be converted to ' + arguments.target_extension.value + ' extension and be kept in the "' + arguments.deleted_folder.value + '" folder.\n')

        videos = Search(arguments)
        videos.search()

