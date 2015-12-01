import re


FLAG_REGEX = re.compile(r"-(?P<flag>\w+)=(?P<value>[^ ]+)")


def parser_args(args):
    if not args:
        return {}
    
    flags = {}
    flags['command'] = args[0]

    for arg in args[1:]:
        match = FLAG_REGEX.search(arg)
        if match:
            flags[match.group('flag')] = match.group('value')

    return flags
