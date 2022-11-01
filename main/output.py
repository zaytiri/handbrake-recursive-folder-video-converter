from datetime import date, datetime

from main.services.file import File
from main.utils.bytes_conversion import set_converted_bytes_with_label


class Output:
    """
    output and statistics?
    """
    original_files_size = 0.0
    reduced_files_size = 0.0
    files_not_encoded = []

    def __init__(self, absolute_path_parent):
        self.file = File(absolute_path_parent + '\\output.txt')
        self.file.open('a')

    def add_file_information(self, video_file, successful):
        self.__add_line('[' + str(datetime.utcnow()) + ']\nThe following video file was converted: ' + video_file.name_only)

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
        self.__add_line('[' + str(datetime.utcnow()) + ']\nFinal Statistics:')
        self.__set_message_with_size('\tOriginal size of all searched video files: ', self.original_files_size)
        self.__set_message_with_size('\tReduced size of all converted video files: ', self.reduced_files_size)

        space_saved = self.original_files_size - self.reduced_files_size
        self.__set_message_with_size('\tSpace in disk saved: ', space_saved)

        if len(self.files_not_encoded) != 0:
            self.__add_line('\n\tThe following video files were not encoded successfully:')
        for files in self.files_not_encoded:
            self.__add_line('\t--> ' + files)

        self.file.close()

    def __set_message_with_size(self, message, size):
        size_with_label = set_converted_bytes_with_label(size)
        self.__add_line(message + '%.2f' % size_with_label['size'] + ' ' + size_with_label['label'])

    def __add_line(self, message):
        self.file.write(message + '\n')
