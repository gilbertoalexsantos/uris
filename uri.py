import sys
from uri_parser import parser_args
from uri_submission import run_submissions
from uri_setup import run_setup
from uri_submit import run_submit


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
