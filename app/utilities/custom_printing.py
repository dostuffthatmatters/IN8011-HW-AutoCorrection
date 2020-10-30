import json


class CustomPrinting(object):
    """
    Singleton Class

    This is an abstract class for advanced print statements (in color, bold, underlined)

    Usage:
    print(text) --> CustomPrinting.print_ok_blue(text)

    Suppress new line with:
    CustomPrinting.print_ok_blue(text, new_line=False)

    Available methods:
    print
    print_ok_blue
    print_ok_green
    print_ok_warning
    print_ok_fail
    print_ok_header
    print_ok_bold
    print_ok_underline
    """

    ENDC = '\033[0m'

    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'

    HEADER = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def print(text, new_lines=1, bold=False, underline=False):
        if bold:
            text = CustomPrinting.get_string_bold(text)
        if underline:
            text = CustomPrinting.get_string_underline(text)

        print(str(text), end=("\n"*new_lines if new_lines > 0 else ""))

    @staticmethod
    def print_blue(text, new_lines=1, bold=False, underline=False):
        begin = CustomPrinting.OKBLUE
        end = CustomPrinting.ENDC

        if bold:
            text = CustomPrinting.get_string_bold(text)
        if underline:
            text = CustomPrinting.get_string_underline(text)

        print(begin + str(text) + end, end=("\n"*new_lines if new_lines > 0 else ""))

    @staticmethod
    def print_green(text, new_lines=1, bold=False, underline=False):
        begin = CustomPrinting.OKGREEN
        end = CustomPrinting.ENDC

        if bold:
            text = CustomPrinting.get_string_bold(text)
        if underline:
            text = CustomPrinting.get_string_underline(text)

        print(begin + str(text) + end, end=("\n"*new_lines if new_lines > 0 else ""))

    @staticmethod
    def print_yellow(text, new_lines=1, bold=False, underline=False):
        begin = CustomPrinting.WARNING
        end = CustomPrinting.ENDC

        if bold:
            text = CustomPrinting.get_string_bold(text)
        if underline:
            text = CustomPrinting.get_string_underline(text)

        print(begin + str(text) + end, end=("\n"*new_lines if new_lines > 0 else ""))

    @staticmethod
    def print_red(text, new_lines=1, bold=False, underline=False):
        begin = CustomPrinting.FAIL
        end = CustomPrinting.ENDC

        if bold:
            text = CustomPrinting.get_string_bold(text)
        if underline:
            text = CustomPrinting.get_string_underline(text)

        print(begin + str(text) + end, end=("\n"*new_lines if new_lines > 0 else ""))

    @staticmethod
    def print_pink(text, new_lines=1, bold=False, underline=False):
        begin = CustomPrinting.HEADER
        end = CustomPrinting.ENDC

        if bold:
            text = CustomPrinting.get_string_bold(text)
        if underline:
            text = CustomPrinting.get_string_underline(text)

        print(begin + str(text) + end, end=("\n"*new_lines if new_lines > 0 else ""))

    @staticmethod
    def print_dict(dictionary):
        print(json.dumps(dictionary, indent=4))

    @staticmethod
    def get_string_bold(text):
        return CustomPrinting.BOLD + str(text) + CustomPrinting.ENDC

    @staticmethod
    def get_string_underline(text):
        return CustomPrinting.UNDERLINE + str(text) + CustomPrinting.ENDC


if __name__ == "__main__":

    print("")

    CustomPrinting.print("This is a test print (white)")
    CustomPrinting.print("This is a test print (white, bold)", bold=True)
    CustomPrinting.print("This is a test print (white, bold, underlined)", bold=True, underline=True)

    print("")

    CustomPrinting.print_green("This is a test print (green)")
    CustomPrinting.print_green("This is a test print (green, bold)", bold=True)
    CustomPrinting.print_green("This is a test print (green, bold, underlined)", bold=True, underline=True)

    print("")

    CustomPrinting.print_blue("This is a test print (blue)")
    CustomPrinting.print_blue("This is a test print (blue, bold)", bold=True)
    CustomPrinting.print_blue("This is a test print (blue, bold, underlined)", bold=True, underline=True)

    print("")

    CustomPrinting.print_yellow("This is a test print (yellow)")
    CustomPrinting.print_yellow("This is a test print (yellow, bold)", bold=True)
    CustomPrinting.print_yellow("This is a test print (yellow, bold, underlined)", bold=True, underline=True)

    print("")

    CustomPrinting.print_red("This is a test print (red)")
    CustomPrinting.print_red("This is a test print (red, bold)", bold=True)
    CustomPrinting.print_red("This is a test print (red, bold, underlined)", bold=True, underline=True)

    print("")

    CustomPrinting.print_pink("This is a test print (pink)")
    CustomPrinting.print_pink("This is a test print (pink, bold)", bold=True)
    CustomPrinting.print_pink("This is a test print (pink, bold, underlined)", bold=True, underline=True)
