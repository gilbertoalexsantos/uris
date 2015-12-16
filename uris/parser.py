import re
import os


FLAG_VALUE_REGEX = re.compile(r"-(?P<flag>\w+)=\"?(?P<value>[^\"]*)\"?")
FLAG_ALONE_REGEX = re.compile(r"--(?P<flag>\w+)")


def parser_args(args):
    if not args:
        return {}
    
    flags = {
        'command': args[0],
        'others': []
    }

    for arg in args[1:]:
        match_value = FLAG_VALUE_REGEX.search(arg)
        match_alone = FLAG_ALONE_REGEX.search(arg)
        if match_value:
            flags[match_value.group('flag')] = match_value.group('value')
        elif match_alone:
            flags[match_alone.group('flag')] = True
        else:
            flags['others'].append(arg)


    return flags
