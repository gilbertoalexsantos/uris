from .login import setup_login


def execute_setup_command(flags):
    logged = setup_login()
    while not logged:
        logged = setup_login()
    print "Setup configurated. Bateu ai?"
