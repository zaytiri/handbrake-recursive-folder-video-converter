import subprocess

from havc.entities.video_file import VideoFile
from havc.output import Output
from havc.services.directory import Directory
from havc.command import Command


class Search:
    def __init__(self, arguments):
        self.folder_path = arguments.folder_path_to_convert.value
        self.root_path = arguments.root.value
        self.original_file_extensions = arguments.original_extensions.value
        self.target_file_extension = arguments.target_extension.value
        self.to_delete_folder_name = arguments.deleted_folder.value
        self.custom_command = arguments.custom_command.value
        self.shutdown_when_done = arguments.shutdown_when_done.value

    def search(self):
        main_directory = Directory(self.folder_path)
        output_file = Output(main_directory.root)
        found_files = False

        new_main_delete_folder = self.create_main_delete_folder()

        for root, dirs, files in main_directory.search_through():
            if self.to_delete_folder_name in root:
                continue

            for video in files:
                current_video_file = VideoFile(video, root, self.original_file_extensions, self.target_file_extension)

                if not current_video_file.process():
                    continue

                found_files = True
                handbrake = Command(self.root_path)

                if self.custom_command.upper() != 'off'.upper():
                    handbrake.set_custom_command(self.custom_command)

                successful = handbrake.run_command(current_video_file)

                sub_delete_folder = self.create_delete_folder_structure(root, new_main_delete_folder)

                if successful:
                    current_video_file.copy_to(sub_delete_folder)

                output_file.add_file_information(current_video_file, successful)

        output_file.add_final_output()

        if not found_files:
            print('\nNo files were found with current extensions.')
            output_file_to_delete = Directory(output_file.file.path)
            output_file_to_delete.remove()

        if self.shutdown_when_done:
            subprocess.run(["shutdown", "-s"])

    def create_main_delete_folder(self):
        root_directory = Directory(self.folder_path)
        new_delete_directory = Directory(root_directory.last_folder_path)
        to_delete_folder_path = new_delete_directory.create_folder(self.to_delete_folder_name)
        return Directory(to_delete_folder_path)

    def create_delete_folder_structure(self, root, new_deleted_folder_directory):
        root_directory = Directory(self.folder_path)
        last_directory = Directory(root_directory.last_folder_path)
        to_delete_folder = last_directory.root
        path_name_list = root.split('\\')
        for folder in path_name_list:
            if folder == last_directory.current_folder:
                to_delete_folder = to_delete_folder + '\\' + new_deleted_folder_directory.current_folder
            if folder not in to_delete_folder:
                to_delete_folder = to_delete_folder + '\\' + folder

        return new_deleted_folder_directory.create_folder(to_delete_folder)
