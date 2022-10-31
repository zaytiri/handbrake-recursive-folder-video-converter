from main.services.file import File


class Output:
    """
    output and statistics?
    """
    original_files_size = 0.0
    reduced_files_size = 0.0

    def __init__(self, absolute_path_parent):
        self.file = File(absolute_path_parent + '\\output.txt')
        self.file.open('a')

    def add_file_information(self, video_file):
        self.add_line('The following video file is converted: ' + video_file.name_only)
        self.add_line('\tThe absolute path is: ' + video_file.absolute_path)
        self.add_line('\tThe original extension was: ' + video_file.extension)
        self.add_line('\tThe target extension was: ' + video_file.target_extension)
        self.add_line('\tThe original file size was: %.2f' % self.__convert_bytes(video_file.original_size) + self.__get_bytes_label(video_file.original_size))
        self.add_line('\tThe converted file size is: %.2f' % self.__convert_bytes(video_file.converted_size) + self.__get_bytes_label(
            video_file.converted_size))
        self.add_line('\n\n')

        self.original_files_size += video_file.original_size
        self.reduced_files_size += video_file.converted_size

    def add_final_output(self):
        self.add_line('\n\nFinal Statistics:')
        self.add_line('Original size of all searched video files: %.2f' % self.__convert_bytes(self.original_files_size) + self.__get_bytes_label(
            self.original_files_size))
        self.add_line('Reduced size of all converted video files: %.2f' % self.__convert_bytes(self.reduced_files_size) + self.__get_bytes_label(
            self.reduced_files_size))
        self.file.close()

    def add_line(self, message):
        self.file.write(message + '\n')

    # todo: refactor the following static methods
    @staticmethod
    def __convert_bytes(size_in_bytes):
        kilobyte = 1024
        megabyte = kilobyte * kilobyte
        gigabyte = megabyte * kilobyte

        if kilobyte < size_in_bytes < megabyte:
            converted_size = size_in_bytes / kilobyte
        elif megabyte < size_in_bytes < gigabyte:
            converted_size = size_in_bytes / megabyte
        elif size_in_bytes >= gigabyte:
            converted_size = size_in_bytes / gigabyte
        else:
            converted_size = size_in_bytes

        return converted_size

    @staticmethod
    def __get_bytes_label(size):
        kilobyte = 1024
        megabyte = kilobyte * kilobyte
        gigabyte = megabyte * kilobyte

        if kilobyte < size < megabyte:
            label = 'KB'
        elif megabyte < size < gigabyte:
            label = 'MB'
        elif size >= gigabyte:
            label = 'GB'
        else:
            label = 'B'

        return label
