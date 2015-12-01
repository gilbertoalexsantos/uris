from uri_login import setup_login


def run_setup(flags):
    logged = setup_login()
    while not logged:
        logged = setup_login()
    print "Setup configurated. Bateu ai?"
