from datetime import datetime

from main.services.file import File


class Output:
    """
    output and statistics?
    """
    original_files_size = 0.0
    reduced_files_size = 0.0
    size_with_label = {}
    files_not_encoded = []

    def __init__(self, absolute_path_parent):
        self.file = File(absolute_path_parent + '\\output.txt')
        self.file.open('a')

    def add_file_information(self, video_file, successful):
        self.__add_line('[' + str(datetime.now()) + ']\nThe following video file was converted: ' + video_file.name_only)

        if not successful:
            self.__add_line('\t*** This file was not encoded successfully! ***\n')
            self.files_not_encoded.append(video_file.absolute_path + video_file.extension)
            return

        self.__add_line('\t-Converted from ' + video_file.extension + ' extension to ' + video_file.target_extension)
        self.__set_message_with_size('\t-The original file size was: ', video_file.original_size)
        self.__set_message_with_size('\t-The converted file size is: ', video_file.converted_size)

        self.__add_line('\n')

        self.original_files_size += video_file.original_size
        self.reduced_files_size += video_file.converted_size

    def add_final_output(self):
        self.__add_line('[' + str(datetime.now()) + ']\nFinal Statistics:')
        self.__set_message_with_size('\tOriginal size of all searched video files: ', self.original_files_size)
        self.__set_message_with_size('\tReduced size of all converted video files: ', self.reduced_files_size)

        space_saved = self.original_files_size - self.reduced_files_size
        self.__set_message_with_size('\tSpace in disk saved: ', space_saved)

        self.__add_line('\n\tThe following video files were not encoded successfully:')
        for files in self.files_not_encoded:
            self.__add_line('\t--> ' + files)
        self.file.close()

    def __set_message_with_size(self, message, size):
        self.__set_converted_bytes_with_label(size)
        self.__add_line(message + '%.2f' % self.size_with_label['size'] + ' ' + self.size_with_label['label'])

    def __add_line(self, message):
        self.file.write(message + '\n')

    def __set_converted_bytes_with_label(self, size_in_bytes):
        kilobyte = 1024
        megabyte = kilobyte * kilobyte
        gigabyte = megabyte * kilobyte

        if kilobyte < size_in_bytes < megabyte:
            converted_size = size_in_bytes / kilobyte
            label = 'KB'
        elif megabyte < size_in_bytes < gigabyte:
            converted_size = size_in_bytes / megabyte
            label = 'MB'
        elif size_in_bytes >= gigabyte:
            converted_size = size_in_bytes / gigabyte
            label = 'GB'
        else:
            converted_size = size_in_bytes
            label = 'B'

        self.size_with_label = {'size': converted_size, 'label': label}
