from ..blucrawler import get_results_from_crawler
from ..urispider.spiders.submit import SubmitSpider
from ..login import get_login_form_data, logged
from ..util import get_file_from_path
from ..parser import match_single_double_key


brief_description = """\
uris sub[mit] [-lang | --language] [-c | --code] [-s | --source]
"""


help_description = """\
Command:
  {}

All the three flags are required.

The language flag accept the options:
  c    C
  c++  C++
  java Java
  py2  Python 2
  py3  Python 3

The code flag is the ID of the problem.

The source flag is source code path.

Examples of execution:
  uris sub -lang=java -c=1399 -s=uri-1399.java
  uris sub -lang=c++ --code=1888 --source="/Users/gilberto/My Codes/source.cpp"
  uris submit --language=py2 --code=1000 --source=My\ Source\ Code.py\
""".format(brief_description)


form_data_key = {
    'problem': 'data[Run][problem_id]',
    'language': 'data[Run][language_id]',
    'source': 'data[Run][source_code]'
}


type_of_language = {
    'c': ("C", "1"),
    'c++': ("C++", "2"),
    'java': ("Java", "3"),
    'py2': ("Python 2", "4"),
    'py3': ("Python 3", "5"),
}


def get_form_data(flags):
    form_data = {}

    code_value = match_single_double_key(flags, 'c', 'code')
    if code_value:
        form_data[form_data_key['problem']] = code_value


    language_value = match_single_double_key(flags, 'lang', 'language')
    if language_value:
        language = type_of_language.get(language_value, None)
        if language:
            form_data[form_data_key['language']] = language[1]

    source_value = match_single_double_key(flags, 's', 'source')
    if source_value:
        source_code = get_file_from_path(source_value)
        form_data[form_data_key['source']] = source_code

    return form_data


@logged
def run_submit(flags):
    result = get_results_from_crawler(SubmitSpider,
                                      submit_form_data=get_form_data(flags),
                                      login_form_data=get_login_form_data())
    if result and result[0]['submited']:
        print "Successful! (The submission of course)"
    else:
        print "Something went wrong with the submission... I'm sorry, I guess..."


def execute_submit_command(flags):
    if 'help' in flags['double']:
        print help_description
    else:
        run_submit(flags)
