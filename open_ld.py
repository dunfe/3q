import subprocess
import os.path
from subprocess import Popen

ldconsole = r'D:\Application\LDPlayer\LDPlayer4.0\ldconsole.exe'


def open_ld_player():
    ld_console_exist = check_ld_console()

    if not ld_console_exist:
        exit()

    ld_existed = check_ld()

    if not ld_existed:
        created = create_ld()

    open_ld()


def open_ld():
    print('Opening LDPlayer')
    p = Popen([ldconsole, 'launch', '--index', '0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
              universal_newlines=True)
    output, errors = p.communicate()
    print(output)


def create_ld():
    p = Popen([ldconsole, "add"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
              universal_newlines=True)

    output, errors = p.communicate()

    if len(output) > 0:
        return True

    print(errors)
    return False


def check_ld_console():
    if os.path.isfile(ldconsole):
        print("File exist")
        return True
    else:
        print("File not exist")
        return False


def check_ld():
    p = Popen([ldconsole, "list2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
              universal_newlines=True)

    output, errors = p.communicate()

    if len(output) > 0:
        print('LDPlayer exist')
        return True

    print(errors)
    return False
