import sys
from uri_parser import parser_args
from uri_submission import run_submissions
from uri_setup import run_setup


commands = {
    'setup': run_setup,
    'subs': run_submissions
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


command_fn(flags)
