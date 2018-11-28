import sys
import platform

from colorama import Fore, init

if platform.system() != 'Linux':
    init(convert=True)


class Cast:

    def clear_last_line(self):
        if self.last_type not in self.erase_exceptions and 'all' not in self.erase_exceptions:
            sys.stdout.write('\x1b[1A\x1b[2K')

    def __init__(self, status, startup_message='Starting', complete_message='Done', fail_message='Failed',
                 erase_exceptions=None):
        if erase_exceptions is None:
            erase_exceptions = ['fail', 'error']
        self.status = status
        self.startup_message = startup_message
        self.complete_message = complete_message
        self.fail_message = fail_message
        self.erase_exceptions = erase_exceptions
        self.last_type = None
        self.start()

    def start(self):
        print('{} {}'.format(self.status, Fore.LIGHTYELLOW_EX + self.startup_message + Fore.RESET))
        self.last_type = 'start'

    def info(self, info):
        self.clear_last_line()
        print('{} {}'.format(self.status, Fore.LIGHTBLUE_EX + 'Info' + Fore.RESET + ': '
                             + Fore.LIGHTBLUE_EX + info + Fore.RESET))
        self.last_type = 'info'

    def complete(self, complete_message=None):
        if not complete_message:
            complete_message = self.complete_message

        self.clear_last_line()
        print('{} {}'.format(self.status, Fore.LIGHTGREEN_EX + complete_message + Fore.RESET))
        self.last_type = 'complete'

    def error(self, error_message):
        self.clear_last_line()
        text = '{} {}'.format(self.status, Fore.LIGHTRED_EX + 'Error' + Fore.RESET + ': '
                              + Fore.LIGHTRED_EX + error_message + Fore.RESET)
        if sys.stdout.isatty():
            print(text)
        else:
            sys.stderr.write(text)
        self.last_type = 'error'

    def fail(self, error_message, status_code=1):
        self.clear_last_line()
        text = '{} {}'.format(self.status, Fore.LIGHTRED_EX + 'Failed' + Fore.RESET + ': '
                              + Fore.LIGHTRED_EX + error_message + Fore.RESET)
        if sys.stdout.isatty():
            print(text)
        else:
            sys.stderr.write(text)
        self.last_type = 'fail'
        quit(status_code)
