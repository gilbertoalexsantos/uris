import os


def get_file_from_path(path):
    source_code = ""
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(path):
        return source_code
    with open(path) as f:
        source_code = f.read()
    return source_code


def get_extension_from_path(path):
    if not os.path.isfile(path):
        return None
    extension = os.path.splitext(path)[1]
    return extension[1:]


def get_home_path():
    return os.path.expanduser('~')
