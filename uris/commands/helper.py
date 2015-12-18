from .submission import brief_description as submission_brief_description
from .submit import brief_description as submit_brief_description
from .setup import brief_description as setup_brief_description
from .last_submission import brief_description as last_submission_brieft_description


brief_description = """\
uris help\
"""

help_description = """\
If you want detailed explanation about a command, use the --help flag.

Example:
  uris subs --help
  uris last --help

Commands:
  Submissions
    {submissions}
  Last submission
    {last_submission}
  Submit a problem
    {submit}
  Setup settings
    {setup}
  Helper
    {helper}\
""".format(
    submissions=submission_brief_description,
    last_submission=last_submission_brieft_description,
    submit=submit_brief_description,
    setup=setup_brief_description,
    helper=brief_description
)


def execute_helper_command(flags):
    print help_description
