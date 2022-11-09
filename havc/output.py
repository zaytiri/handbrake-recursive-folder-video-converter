from datetime import date, datetime

from .services.file import File
from .utils.bytes_conversion import set_converted_bytes_with_label


class Output:
    """
    output and statistics?
    """
    original_files_size = 0.0
    reduced_files_size = 0.0
    files_not_encoded = []
    number_of_files_encoded = 0

    def __init__(self, absolute_path_parent):
        date_now = '['+str(date.today().year)+'-'+str(date.today().month)+'-'+str(date.today().day)+' '+str(datetime.utcnow().hour)+'-'+str(
            datetime.utcnow().minute)+']'
        self.file = File(absolute_path_parent + '\\output' + date_now + '.txt')
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
        self.number_of_files_encoded += 1
        self.original_files_size += video_file.original_size
        self.reduced_files_size += video_file.converted_size

    def add_final_output(self):
        self.__add_line('[' + str(datetime.utcnow()) + ']\nFinal Statistics:')
        self.__set_message_with_size('\tOriginal size of all searched video files: ', self.original_files_size)
        self.__set_message_with_size('\tReduced size of all converted video files: ', self.reduced_files_size)

        space_saved = self.original_files_size - self.reduced_files_size
        self.__set_message_with_size('\tSpace in disk saved: ', space_saved)

        number_of_files_not_encoded = len(self.files_not_encoded)
        self.__add_line('\n\t- Total number of files converted: ' + str(self.number_of_files_encoded))
        self.__add_line('\t- Total number of files unsuccessfully converted: ' + str(number_of_files_not_encoded))
        total = self.number_of_files_encoded + number_of_files_not_encoded
        self.__add_line('\t- Total number of files found: ' + str(total))

        if number_of_files_not_encoded != 0:
            self.__add_line('\n\tThe following video files were not encoded successfully:')
        for files in self.files_not_encoded:
            self.__add_line('\t--> ' + files)

        self.file.close()

    def __set_message_with_size(self, message, size):
        size_with_label = set_converted_bytes_with_label(size)
        self.__add_line(message + '%.2f' % size_with_label['size'] + ' ' + size_with_label['label'])

    def __add_line(self, message):
        self.file.write(message + '\n')
