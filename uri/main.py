import sys
import os
from .parser import parser_args
from .setup import run_setup
from .commands.submission import run_submissions
from .commands.submit import run_submit


def execute():
    commands = {
        'setup': run_setup,
        'subs': run_submissions,
        'sub': run_submit
    }


    flags = parser_args(sys.argv[1:])


    command = flags.get('command', None)
    if not command:
        print "Did you type any command? '-'"
        exit(0)


    command_fn = commands.get(command, None)
    if not command_fn:
        print "That command doesn't exist, sorry =/"
        exit(0)

    print "Executing command..."
    command_fn(flags)


if __name__ == '__main__':
    execute()
