from datetime import date, datetime

from havc.services.file import File
from havc.utils.bytes_conversion import set_converted_bytes_with_label


class Output:
    """
    output and statistics?
    """
    original_files_size = 0.0
    reduced_files_size = 0.0
    files_not_encoded = []
    number_of_files_encoded = 0
    skipped_files = []
    video_files = []
    output_file = None

    def __add_file_information(self, timestamp, video_file):
        self.__add_line('[' + str(timestamp) + ']\nThe following video file was converted: ' + video_file.name_only)

        self.__add_line('\t-Converted from ' + video_file.extension + ' extension to ' + video_file.target_extension)
        self.__set_message_with_size('\t-The original file size was: ', video_file.original_size)
        self.__set_message_with_size('\t-The converted file size is: ', video_file.converted_size)

        self.__add_line('\n')
        self.number_of_files_encoded += 1
        self.original_files_size += video_file.original_size
        self.reduced_files_size += video_file.converted_size

    def add_file(self, video_file):
        self.video_files.append({
            'timestamp': datetime.utcnow(),
            'video_file': video_file
        })

    def add_skipped_file(self, skipped_file_path):
        self.skipped_files.append(skipped_file_path)

    def add_unsuccessful_file(self, unsuccessful_file_path):
        self.files_not_encoded.append(unsuccessful_file_path)

    def process(self, absolute_path_parent):
        date_now = '[' + str(date.today().year) + '-' + str(date.today().month) + '-' + str(date.today().day) + ' ' + str(
            datetime.utcnow().hour) + '-' + str(
            datetime.utcnow().minute) + '-' + str(datetime.utcnow().second) + ']'
        self.output_file = File(absolute_path_parent + '\\output' + date_now + '.txt')
        self.output_file.open('a')

        for video_file in self.video_files:
            self.__add_file_information(video_file['timestamp'], video_file['video_file'])

        self.__add_line('[' + str(datetime.utcnow()) + ']\nFinal Statistics:')
        self.__set_message_with_size('\tSize of all original video files: ', self.original_files_size)
        self.__set_message_with_size('\tSize of all converted video files: ', self.reduced_files_size)

        space_saved = self.original_files_size - self.reduced_files_size
        if space_saved > 0:
            self.__set_message_with_size('\tSpace in disk saved: ', space_saved)

        number_of_files_not_encoded = len(self.files_not_encoded)
        self.__add_line('\n\t- Total number of files converted: ' + str(self.number_of_files_encoded))
        self.__add_line('\t- Total number of files unsuccessfully converted: ' + str(number_of_files_not_encoded))
        total = self.number_of_files_encoded + number_of_files_not_encoded
        self.__add_line('\t- Total number of files found: ' + str(total))
        self.__add_line('\t- Total number of files skipped: ' + str(len(self.skipped_files)))

        if number_of_files_not_encoded != 0:
            self.__add_line('\n\tThe following video files were not encoded successfully:')
            for file in self.files_not_encoded:
                self.__add_line('\t--> ' + file)

        if len(self.skipped_files) > 0:
            self.__add_line('\n\tThe following video files were skipped:')
            for file in self.skipped_files:
                self.__add_line('\t--> ' + file)

        self.output_file.close()

    def __set_message_with_size(self, message, size):
        size_with_label = set_converted_bytes_with_label(size)
        self.__add_line(message + '%.2f' % size_with_label['size'] + ' ' + size_with_label['label'])

    def __add_line(self, message):
        self.output_file.write(message + '\n')
