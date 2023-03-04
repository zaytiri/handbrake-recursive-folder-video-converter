import os
import yaml


def create(self, new_folder):
    return os.path.join(self.root, new_folder)


def create_folder(self, new_folder):
    new_directory = self.create(new_folder)
    if not os.path.isdir(new_directory):
        os.mkdir(new_directory)


def get_version():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'progsettings.yaml')
    with open(path, 'r') as settings_file:
        settings = yaml.safe_load(settings_file)['prog'.upper()]
        return settings['version'.upper()]
