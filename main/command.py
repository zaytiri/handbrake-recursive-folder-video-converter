import shutil
import subprocess


class Command:
    """
    here it will go the future feature about choosing a default command versus a command inserted by the user
    """
    handbrake_command = ''

    def __init__(self, root_path):
        self.root_path = root_path

    def run_command(self, file_info, target_extension):
        print('Current Command: ' + ' '.join([str(elem) for elem in self.__basic_command(file_info, target_extension)]) + '\n')

        process = subprocess.run(self.__basic_command(file_info, target_extension), stderr=subprocess.PIPE)

        error = process.stderr.decode()
        result = "Encode done!" in str(error)

        return result

    def __basic_command(self, file_info, target_extension):
        exe = self.root_path + '\\HandBrakeCLI.exe'
        basic_command = [exe, '--preset', 'Very Fast 1080p30', '-i', '{}'.format(file_info.absolute_path) + \
                         file_info.extension, '-o', '{}'.format(file_info.absolute_path) + \
                         target_extension]

        return basic_command
