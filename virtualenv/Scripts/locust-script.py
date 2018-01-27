#!f:\mypython\flaskwebapp\virtualenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'locust==0.8','console_scripts','locust'
__requires__ = 'locust==0.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('locust==0.8', 'console_scripts', 'locust')()
    )
