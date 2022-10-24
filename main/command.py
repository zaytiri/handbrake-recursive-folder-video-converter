import subprocess

"""
here it will go th future feature about choosing a default comand versus a command inserted by the user
"""
class Command:
    command = ''

    def __init__(self, rootPath):
        self.rootPath = rootPath

    def run_command(self, fileInfo, targetExtension):
        print('Current Command: ' + self.__basic_command(fileInfo, targetExtension) + '\n')

        s = subprocess.run(self.__basic_command(fileInfo, targetExtension), shell=True, cwd=self.rootPath)
        print(s)

    def __basic_command(self, fileInfo, targetExtension):
        return '.\\HandBrakeCLI.exe --preset "Very Fast 1080p30" -i "{}'.format(fileInfo.absolutePath) + \
               fileInfo.extension + '" -o "{}'.format(fileInfo.absolutePath) + \
               targetExtension + '"'

