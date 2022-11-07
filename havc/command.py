import subprocess

from .utils.split_string import split_string


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
        if self.custom_command is None:
            process = self.__run_static_command(file_info)
        else:
            process = self.__run_custom_command(file_info)

        result = "Encode done!" in str(process)
        return result

    def __run_static_command(self, file_info):
        return self.__run(self.__basic_command(file_info))

    def __run_custom_command(self, file_info):
        list_of_args = split_string(self.custom_command, ' ', '\'')

        list_of_args[list_of_args.index(self.original_file_placeholder)] = file_info.absolute_path + file_info.extension
        list_of_args[list_of_args.index(self.converted_file_placeholder)] = file_info.absolute_path + file_info.target_extension

        list_of_args.insert(0, self.handbrake_executable)

        return self.__run(list_of_args)

    def __basic_command(self, file_info):
        basic_command = [
            self.handbrake_executable,
            '--preset', 'Very Fast 1080p30',
            '-i',
            file_info.absolute_path + file_info.extension,
            '-o',
            file_info.absolute_path + file_info.target_extension
        ]

        return basic_command

    @staticmethod
    def __run(args):
        print('Current Command: ' + ' '.join([str(elem) for elem in args]) + '\n')
        return subprocess.run(args, stderr=subprocess.PIPE)
