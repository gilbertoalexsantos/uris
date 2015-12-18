from ..blucrawler import get_results_from_crawler
from ..urispider.spiders.submissions import SubmissionSpider
from ..login import get_login_form_data, logged
from ..parser import match_single_double_key


brief_description = """\
uris [subs | submissions] [-lang | --language] [-a | --answer] [-c | --code]\
"""


help_description = """\
Command:
  {}

All flags are optional

The language flag accept the options:
  c    C
  c++  C++
  java Java
  py2  Python 2
  py3  Python 3

The answer flag accept the options:
  ac   Accepted
  ce   Compilation Error
  re   Runtime Error
  tle  Time Limit Exceed
  pe   Presentation Error
  wa   Wrong Answer

The code flag is the ID of the problem.

Examples of execution:
  uris subs
  uris subs -lang=c -a=tle -c=1399
  uris submissions --language=java -a=wa\
""".format(brief_description)


fields = ('id_problem', 'name_problem', 'answer', 'language', 'time', 'date')


submission_line_format = u'{:<8}{:<28}{:<20}{:^10}{:^10}{:^23}'


form_data_key = {
    'problem': 'data[filter][problem]',
    'answer': 'data[filter][answer]',
    'language': 'data[filter][language]',
}


type_of_answer = {
    'ac': ("Accepted", "1"),
    'ce': ("Compilation Error", "2"),
    're': ("Runtime Error", "3"),
    'tle': ("Time Limit Exceed", "4"),
    'pe': ("Presentation Error", "5"),
    'wa': ("Wrong Answer", "6"),
}


type_of_language = {
    'c': ("C", "1"),
    'c++': ("C++", "2"),
    'java': ("Java", "3"),
    'py2': ("Python 2", "4"),
    'py3': ("Python 3", "5"),
}


def print_submission_items(items):
    print submission_line_format.format('Code', 'Problem', 'Answer',
                                        'Language', 'Time', 'Date')
    for item in items:
        print submission_line_format.format(*[item[key] for key in fields])


def get_form_data(flags):
    form_data = {}

    answer_value = match_single_double_key(flags, 'a', 'answer')
    if answer_value:
        answer = type_of_answer.get(answer_value, None)
        if answer:
            form_data[form_data_key['answer']] = answer[1]

    language_value = match_single_double_key(flags, 'lang', 'language')
    if language_value:
        language = type_of_language.get(language_value, None)
        if language:
            form_data[form_data_key['language']] = language[1]

    code_value = match_single_double_key(flags, 'c', 'code')
    if code_value:
        form_data[form_data_key['problem']] = code_value

    return form_data


@logged
def run_submissions(flags):
    results = get_results_from_crawler(SubmissionSpider,
                                       submissions_form_data=get_form_data(flags),
                                       login_form_data=get_login_form_data())
    print_submission_items(results)


def execute_submissions_command(flags):
    if 'help' in flags['double']:
        print help_description
    else:
        run_submissions(flags)
