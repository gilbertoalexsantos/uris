import re
import os


FLAG_VALUE_REGEX = re.compile(r"-?-(?P<flag>\w+)(=\"?(?P<value>[^\"]*)\"?)?")


def match_single_double_key(flags, single_key, double_key):
    if single_key in flags['single']:
        return flags['single'][single_key]
    if double_key in flags['double']:
        return flags['double'][double_key]
    return None


def is_a_arg(arg):
    if len(arg) < 2:
        return False
    qt_dash = sum([1 if char == '-' else 0 for char in arg[0:3]])
    return 1 <= qt_dash <= 2


def is_double_arg(arg):
    return len(arg) >= 2 and arg[0] == '-' and arg[1] == '-'


def parser_args(args):
    if not args:
        return {}
    
    flags = {
        'command': args[0],
        'single': {},
        'double': {},
        'others': []
    }

    for arg in args[1:]:
        match_value = FLAG_VALUE_REGEX.search(arg)
        if is_a_arg(arg) and match_value:
            value = match_value.group('value')
            value = value if value else True
            if is_double_arg(arg):
                flags['double'][match_value.group('flag')] = value
            else:
                flags['single'][match_value.group('flag')] = value
        else:
            flags['others'].append(arg)

    return flags
