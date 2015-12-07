from blucrawler import get_results_from_crawler
from urispider.spiders.submit import SubmitSpider
from uri_login import get_login_form_data, logged
import uri_util


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


def pre_process_flags(flags):
    if 'sc' in flags:
        flags['sc'] = uri_util.get_file_from_path(flags['sc'])


def get_form_data(flags):
    pre_process_flags(flags)
    
    form_data = {}

    if 'code' in flags:
        form_data[form_data_key['problem']] = flags['code']

    if 'ln' in flags:
        language = type_of_language.get(flags['ln'], None)
        if language:
            form_data[form_data_key['language']] = language[1]

    if 'sc' in flags:
        form_data[form_data_key['source']] = flags['sc']

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
