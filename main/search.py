from entities.video_file import VideoFile
from entities.directory import Directory
from command import Command


class Search:
    def __init__(self, arguments):
        self.folder_path = arguments.folder_path_to_convert.value
        self.root_path = arguments.root.value
        self.original_file_extensions = arguments.original_extensions.value
        self.target_file_extension = arguments.target_extension.value
        self.to_delete_folder_name = arguments.deleted_folder.value

    def search(self):
        main_directory = Directory(self.folder_path)
        for root, dirs, files in main_directory.search_through():
            if self.to_delete_folder_name in root:
                continue

            for video in files:
                current_video_file = VideoFile(video, self.folder_path, self.original_file_extensions)

                if current_video_file.process():
                    print('Current current_video_file being converted: ' + current_video_file.name_only)

                    handbrake = Command(self.root_path)
                    handbrake.run_command(current_video_file, self.target_file_extension)

                    root_directory = Directory(root)

                    new_delete_directory = Directory(root_directory.last_folder_path)
                    to_delete_folder_path = new_delete_directory.create_folder(self.to_delete_folder_name)

                    new_deleted_folder_directory = Directory(to_delete_folder_path)
                    new_deleted_folder_path = new_deleted_folder_directory.create_folder(root_directory.current_folder)

                    current_video_file.copy_to(new_deleted_folder_path)
