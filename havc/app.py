import sys

from arguments import Arguments
from search import Search


def main():
    arguments = Arguments().configure()

    print('All files found with the a ', end="")
    first = True
    for extension in arguments.original_extensions.value:
        if first:
            print(extension, end="")
            first = False
            continue
        print(' or ' + extension, end="")
    print(
        ' extension are going to be converted to ' + arguments.target_extension.value + ' extension and be kept in the "' + arguments.deleted_folder.value + '" folder.')
    print('"' + arguments.folder_path_to_convert.value + '" is going to be modified permanently.\n')

    videos = Search(arguments)

    if arguments.safety_question.value:
        response = input(
            'Are you sure you want to continue? \n [Y/n]')
        if response == 'n' or response == 'N':
            sys.exit()
        elif response == 'Y':
            videos.search()
            return

    videos.search()

