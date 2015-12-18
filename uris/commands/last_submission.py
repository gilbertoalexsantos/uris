from ..blucrawler import get_results_from_crawler
from ..urispider.spiders.submissions import SubmissionSpider
from ..login import get_login_form_data, logged
from .submission import print_submission_items


brief_description = """\
uris last [QT_SUBMISSIONS]\
"""

help_description = """\
Command:
  {}

You can specify the number of submissions you want. The default is 1.

Example:
  uris last
  uris last 5\
""".format(brief_description)

@logged
def run_last_submission(flags):
    results = get_results_from_crawler(SubmissionSpider,
                                       submissions_form_data={},
                                       login_form_data=get_login_form_data())

    qt_results = 1
    if 'others' in flags and flags['others']:
        try:
            qt_results = int(flags['others'][0])
        except Exception:
            pass
    if qt_results <= 0:
        qt_results = 1

    results = results[0:qt_results]
    print_submission_items(results)


def execute_last_submission_command(flags):
    if 'help' in flags:
        print help_description
    else:
        run_last_submission(flags)
