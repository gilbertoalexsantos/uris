from .submission import brief_description as submission_brief_description
from .submit import brief_description as submit_brief_description
from .setup import brief_description as setup_brief_description


brief_description = """\
uri help\
"""


def execute_helper_command(flags):
    print "Last submissions:"
    print "  ", submission_brief_description

    print "Submit a problem:"
    print "  ", submit_brief_description

    print "Setup settings:"
    print "  ", setup_brief_description

    print "Helper:"
    print "  ", brief_description
