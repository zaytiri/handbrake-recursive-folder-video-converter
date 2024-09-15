from havc.entities.video_file import VideoFile
from havc.output import Output
from havc.services.directory import Directory
from havc.command import Command
from havc.utils.operating_system import OperatingSystem


class Search:
    def __init__(self, arguments):
        self.folder_path = arguments.folder_path_to_convert.value
        self.root_path = arguments.root.value
        self.original_file_extensions = arguments.original_extensions.value
        self.target_file_extension = arguments.target_extension.value
        self.delete_folder = arguments.deleted_folder.value
        self.custom_command = arguments.custom_command.value

    def search(self):
        main_directory = Directory(self.folder_path)
        output_file = Output()
        found_files = False

        delete_folder = self.create_delete_folder()

        for root, dirs, files in main_directory.search_through():
            if self.delete_folder in root:
                continue

            for video in files:
                current_video_file = VideoFile(video, root, self.original_file_extensions, self.target_file_extension)

                if not current_video_file.process():
                    continue

                if current_video_file.already_exists():
                    print(root + OperatingSystem().get_correct_slash_symbol() + video + ' was skipped because file with same name already exists!\n\n')
                    output_file.add_skipped_file(root + OperatingSystem().get_correct_slash_symbol() + video)
                    continue

                found_files = True
                handbrake = Command(self.root_path)

                if self.custom_command.upper() != 'off'.upper():
                    handbrake.set_custom_command(self.custom_command)

                successful = handbrake.run_command(current_video_file)

                if not successful:
                    print('\nEncoding unsuccessful.\n\n')
                    output_file.add_unsuccessful_file(root + OperatingSystem().get_correct_slash_symbol() + video)
                    continue

                print('\nEncoding successfully done!\n\n')
                sub_delete_folder = self.create_delete_sub_folder(root, delete_folder)
                
                converted_video_file_path = current_video_file.absolute_path + self.target_file_extension
                current_video_file.copy_metadata_to(converted_video_file_path)

                current_video_file.copy_to(sub_delete_folder)
                output_file.add_file(current_video_file)

        if found_files:
            output_file.process(main_directory.root)
            print('\nAn output file with a summary was created in the following directory: \n\t\t' + output_file.output_file.path + '')
        else:
            print('\nNo files were found with current extensions.')

    def create_delete_folder(self):
        root_directory = Directory(self.folder_path)
        new_delete_directory = Directory(root_directory.last_folder_path)
        to_delete_folder_path = new_delete_directory.create_folder(self.delete_folder)
        return Directory(to_delete_folder_path)

    def create_delete_sub_folder(self, root, delete_folder):
        delete_folder_path = delete_folder.root
        main_directory = Directory(self.folder_path)

        path_name_list = root.split(OperatingSystem().get_correct_slash_symbol())
        pass_main_folder = False
        for folder in path_name_list:
            if folder == main_directory.current_folder:
                pass_main_folder = True
                
            if pass_main_folder:
                delete_folder_path = delete_folder_path + OperatingSystem().get_correct_slash_symbol() + folder
                delete_folder.create_folder(delete_folder_path)

        return delete_folder_path
