from uri_settings import get_settings, settings_file_exist, create_settings_file
from urispider.spiders.login import LoginSpider
from blucrawler import get_results_from_crawler


form_keys = {
    'login': 'data[User][email]',
    'password': 'data[User][password]'
}


def get_login_form_data():
    settings = get_settings()

    form_data = {}
    
    if 'login' in settings and 'password' in settings:
        form_data[form_keys['login']] = settings['login']
        form_data[form_keys['password']] = settings['password']

    return form_data


def try_to_login(login, password):
    login_form_data = {
        form_keys['login']: login,
        form_keys['password']: password
    }
    login_result = get_results_from_crawler(LoginSpider,
                                            login_form_data=login_form_data)

    if len(login_result) != 1:
        return False

    return login_result[0].get('logged', False)


def check_login():
    if not settings_file_exist():
        return False

    login_form_data = get_login_form_data()
    if not form_keys['login'] in login_form_data or \
       not form_keys['password'] in login_form_data:
        return False

    return True


def setup_login():
    print "Login"
    login = raw_input(">> ")
    print "Password"
    password = raw_input(">> ")
    
    print "Checking if it's correct..."
    
    logged = try_to_login(login, password)
    if not logged:
        print "Your login/password is incorrect. Try again."
        return False

    data = {
        'login': login,
        'password': password
    }

    create_settings_file(data)
    return True


def logged(fn):
    def wrapper(*args, **kwargs):
        if not check_login():
            print "You need to configure your account to use that feature."
            logged = setup_login()
            while not logged:
                logged = setup_login()
            print "Account configurated successful."
        return fn(*args, **kwargs)
    return wrapper
