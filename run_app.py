import subprocess
import time
from subprocess import Popen
from open_ld import ldconsole


def check_ld():

    ld_running = False

    count = 0
    while not ld_running:
        p = Popen([ldconsole, 'isrunning', '--index', '0'],
                  stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                  universal_newlines=True)

        output, errors = p.communicate()
        count = count + 1
        print('Checking lDPlayer attempt: ' + str(count))
        time.sleep(1)
        if count == 300:
            break

        if output == 'running':
            return True

        print(errors)

    return False


def run_app():
    print('Running app')

    running = check_ld()

    if not running:
        print('LDPlayer is not running')
        return

    p = Popen([ldconsole, 'runapp', '--index', '0', '--packagename', 'com.vng.tanomg3q'],
              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
              universal_newlines=True)

    output, errors = p.communicate()
    print(output)
    print(errors)
