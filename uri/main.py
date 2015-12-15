import sys
import os
from .parser import parser_args
from .setup import execute_setup_command
from .commands.submission import execute_submissions_command
from .commands.submit import run_submit
from .commands.helper import execute_helper_command


def execute():
    commands = {
        'setup': execute_setup_command,
        'subs': execute_submissions_command,
        'sub': run_submit,
        'help': execute_helper_command
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
