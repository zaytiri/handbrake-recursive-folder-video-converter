import yaml


def get_version():
    with open('progsettings.yaml', 'r') as settings_file:
        settings = yaml.safe_load(settings_file)['prog'.upper()]
        return settings['version'.upper()]
