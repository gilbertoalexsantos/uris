import sys
import os
from .parser import parser_args
from .commands.setup import execute_setup_command
from .commands.submission import execute_submissions_command
from .commands.submit import execute_submit_command
from .commands.helper import execute_helper_command


def execute():
    commands = {
        'setup': execute_setup_command,
        'subs': execute_submissions_command,
        'sub': execute_submit_command,
        'help': execute_helper_command
    }


    flags = parser_args(sys.argv[1:])


    command = flags.get('command', None)
    if not command:
        print "Did you type any command? '-'"
        sys.exit(0)


    command_fn = commands.get(command, None)
    if not command_fn:
        print "That command doesn't exist, sorry =/"
        print "Type 'uri help' to see the avaiable commands."
        sys.exit(0)


    print "Executing command...\n"
    try:
        command_fn(flags)
    except (KeyboardInterrupt, EOFError) as e:
        print "Bye....."
        sys.exit()


if __name__ == '__main__':
    execute()
