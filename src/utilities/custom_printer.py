import json
import shutil


class CustomPrinter(object):
    """
    This is an abstract class for advanced print statements
    (in color, bold, underlined)

    Example Usage:
    CustomPrinting.print(text, color='blue', new_lines=0, bold=True)

    Available methods:
    print
    print_line
    print_dict
    """

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

    # replacement for a switch statement
    color_functions = {
        'green': lambda text: f"\033[92m{text}\033[0m",
        'yellow': lambda text: f"\033[93m{text}\033[0m",
        'red': lambda text: f"\033[91m{text}\033[0m",
        'pink': lambda text: f"\033[95m{text}\033[0m",
        'blue': lambda text: f"\033[94m{text}\033[0m"
    }

    @staticmethod
    def print(text, color='default', new_lines=1, bold=False, underline=False):

        if isinstance(text, dict):
            CustomPrinter._print_dict(text)
            return

        assert(color in ['default', 'green', 'yellow', 'red', 'pink', 'blue'])
        if color != 'default':
            text = CustomPrinter.color_functions[color](text)

        if bold:
            text = CustomPrinter._get_bold_text(text)
        if underline:
            text = CustomPrinter._get_underlined_text(text)

        print(str(text), end=("" + ("\n"*new_lines)))

    @staticmethod
    def print_line(character='-', color='default', new_lines=1, bold=False):
        assert(len(character) == 1)
        text = character * shutil.get_terminal_size().columns
        assert(color in ['default', 'green', 'yellow', 'red', 'pink', 'blue'])
        if color != 'default':
            text = CustomPrinter.color_functions[color](text)
        if bold:
            text = CustomPrinter._get_bold_text(text)
        print(str(text), end=("\n"*new_lines if new_lines > 0 else ""))

    @staticmethod
    def _print_dict(dictionary):
        print(json.dumps(dictionary, indent=4))

    @staticmethod
    def _get_bold_text(text):
        return CustomPrinter.BOLD + str(text) + CustomPrinter.ENDC

    @staticmethod
    def _get_underlined_text(text):
        return CustomPrinter.UNDERLINE + str(text) + CustomPrinter.ENDC
