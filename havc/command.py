import subprocess

from havc.services.directory import Directory
from havc.utils.error import throw
from havc.utils.split_string import split_string


class Command:
    """
    here it will go the future feature about choosing a default command versus a command inserted by the user
    """
    handbrake_command = ''
    custom_command = None
    original_file_placeholder = '{of}'
    converted_file_placeholder = '{cf}'

    def __init__(self, root_path):
        self.root_path = root_path
        self.handbrake_executable = self.root_path + '\\HandBrakeCLI.exe'

    def set_custom_command(self, custom_command):
        self.custom_command = custom_command

    def run_command(self, file_info):
        executable_path = Directory(self.handbrake_executable)
        if not executable_path.exists():
            throw(executable_path.root + ' path is not valid. either the path is incorrect or HandBrakeCLI.exe file does not exist in this path.')

        if self.custom_command is None:
            process = self.__run_static_command(file_info)
        else:
            process = self.__run_custom_command(file_info)

        return self.__success_of(process)

    def __run_static_command(self, file_info):
        basic_command = [
            self.handbrake_executable,
            '--preset', 'Very Fast 1080p30',
            '-i',
            file_info.absolute_path + file_info.extension,
            '-o',
            file_info.absolute_path + file_info.target_extension
        ]

        return self.__run(basic_command)

    def __run_custom_command(self, file_info):
        list_of_args = split_string(self.custom_command, ' ', '\'')

        list_of_args[list_of_args.index(self.original_file_placeholder)] = file_info.absolute_path + file_info.extension
        list_of_args[list_of_args.index(self.converted_file_placeholder)] = file_info.absolute_path + file_info.target_extension

        list_of_args.insert(0, self.handbrake_executable)

        return self.__run(list_of_args)

    @staticmethod
    def __success_of(process):
        result = 'Encode done!' in str(process)
        return result

    @staticmethod
    def __run(args):
        print('Current Command: ' + ' '.join([str(elem) for elem in args]) + '\n')
        return subprocess.run(args, stderr=subprocess.PIPE)
