from ..blucrawler import get_results_from_crawler
from ..urispider.spiders.submissions import SubmissionSpider
from ..login import get_login_form_data, logged


brief_description = """\
uri subs [-ln=LANGUAGE] [-ans=ANSWER] [-code=PROBLEM_CODE]\
"""


help_description = """\
Command:
  {}

All flags are optional

The ln flag accept the options:
  c    C
  c++  C++
  java Java
  py2  Python 2
  py3  Python 3

The ans flag accept the options:
  ac   Accepted
  ce   Compilation Error
  re   Runtime Error
  tle  Time Limit Exceed
  pe   Presentation Error
  wa   Wrong Answer

The code flag is the ID of the problem.

Examples of execution:
  uri subs
  uri subs -ln=c -ans=tle -code=1399
  uri subs -ln=java -ans=wa\
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

    if 'ans' in flags:
        answer = type_of_answer.get(flags['ans'], None)
        if answer:
            form_data[form_data_key['answer']] = answer[1]

    if 'ln' in flags:
        language = type_of_language.get(flags['ln'], None)
        if language:
            form_data[form_data_key['language']] = language[1]

    if 'code' in flags:
        form_data[form_data_key['problem']] = flags['code']

    return form_data


@logged
def run_submissions(flags):
    results = get_results_from_crawler(SubmissionSpider,
                                       submissions_form_data=get_form_data(flags),
                                       login_form_data=get_login_form_data())
    print_submission_items(results)


def execute_submissions_command(flags):
    if 'help' in flags:
        print help_description
    else:
        run_submissions(flags)
