import os
import shutil

"""
I don't know why but sometimes you need a lot of new_line characters
so that they show any effect inside the markdown preview ...
"""


class CustomMarkdown(object):

    def __init__(self, file_name):
        assert(file_name.endswith(".md"))
        assert(not os.path.isdir(file_name))

        if os.path.isfile(file_name):
            os.remove(file_name)

        open(file_name, 'a').close()

        self.file_name = file_name

    @staticmethod
    def apply_color(text, color):
        if color is None:
            return text
        elif isinstance(color, str):
            return f"<span style='color: {'#' if text[0] != '#' else ''}{color}'>{text}</span>"
        elif isinstance(color, list) or isinstance(color, tuple):
            assert(len(color) == 3)
            return f"<span style='color: rgb({color[0]}, {color[1]}, {color[2]})'>{text}</span>"

    def write_heading(self, text, heading_type='h1', color=None):
        assert(heading_type in ['h1', 'h2', 'h3', 'h4', 'h5'])
        file_object = open(self.file_name, "a")
        file_object.write(
            f"{'#' * int(heading_type[1])} " +
            f"{CustomMarkdown.apply_color(text, color)}\n\n"
        )
        file_object.close()

    def write_codeblock(self, code, language="", new_lines=1):
        file_object = open(self.file_name, "a")
        file_object.write(f"\n```{language}\n")
        file_object.write(f"{code}\n")
        file_object.write(f"```\n\n" + "\n" * new_lines)
        file_object.close()

    def write_text(self, text, bold=False, italic=False, new_lines=0, color=None):
        file_object = open(self.file_name, "a")
        wrapper = ("*" * italic) + ("**" * bold)
        file_object.write(
            f"{wrapper}{CustomMarkdown.apply_color(text, color)}" +
            f"{wrapper}\n" + "\n" * new_lines
        )
        file_object.close()

    def write_horizontal_line(self):
        file_object = open(self.file_name, "a")
        file_object.write(f"\n\n\n---\n\n\n\n\n")
        file_object.close()
