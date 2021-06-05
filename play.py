import subprocess
from subprocess import Popen

adbconsole = r'D:\Application\LDPlayer\LDPlayer4.0\dnconsole.exe'


def click_play_now():
    p = Popen([adbconsole, 'adb', '--index', '0', '--command', 'shell', 'echo', 'TEST'],
              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
              universal_newlines=True)

    output, errors = p.communicate()

    print(output)

