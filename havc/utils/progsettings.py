import os
import yaml


def get_version():
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '\\progsettings.yaml'
    with open(path, 'r') as settings_file:
        settings = yaml.safe_load(settings_file)['prog'.upper()]
        return settings['version'.upper()]
