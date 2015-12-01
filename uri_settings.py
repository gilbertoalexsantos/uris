import json
from os.path import expanduser, isfile, join


settings_file_path = '.uri_settings.json'


def get_home_path():
    return expanduser('~')


def get_settings_path():
    return join(get_home_path(), settings_file_path)


def settings_file_exist():
    return isfile(get_settings_path())


def get_settings():
    with open(get_settings_path()) as settings_file:
        data = json.load(settings_file)
    return data


def create_settings_file(data={}):
    settings_data = {}
    if settings_file_exist():
        settings_data = get_settings()

    for key, value in data.iteritems():
        settings_data[key] = value
        
    with open(get_settings_path(), 'wb+') as settings_file:
        json.dump(settings_data, settings_file)
