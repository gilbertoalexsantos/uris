from ..login import setup_login


brief_description = """\
uris setup\
"""

def execute_setup_command(flags):
    logged = setup_login()
    while not logged:
        logged = setup_login()
    print "Setup configured. Bateu ai?"
