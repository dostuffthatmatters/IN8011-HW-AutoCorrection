import os
import shutil

"""
I don't know why but somehow you crazy many new_line characters
so that they show any effect inside the markdown file...
"""

class CustomMarkdown(object):

    def __init__(self, file_name):
        if file_name.split(".")[-1] != "md":
            raise Exception

        if os.path.isfile(file_name):
            os.remove(file_name)
        elif os.path.isdir(file_name):
            shutil.rmtree(file_name)

        open(file_name, 'a').close()

        self.file_name = file_name

    @staticmethod
    def apply_color(text, color):
        if color is None:
            return text
        elif isinstance(color, str):
            return f"<span style='color: {'#' if text[0] != '#' else ''}{color}'>{text}</span>"
        elif isinstance(color, list) or isinstance(color, tuple):
            return f"<span style='color: rgb({color[0]}, {color[1]}, {color[2]})'>{text}</span>"


    def write_h1(self, text="include_text", color=None):
        file_object = open(self.file_name, "a")
        file_object.write(f"# {CustomMarkdown.apply_color(text, color)}\n\n")
        file_object.close()

    def write_h2(self, text="include_text", color=None):
        file_object = open(self.file_name, "a")
        file_object.write(f"## {CustomMarkdown.apply_color(text, color)}\n\n")
        file_object.close()

    def write_h3(self, text="include_text", color=None):
        file_object = open(self.file_name, "a")
        file_object.write(f"### {CustomMarkdown.apply_color(text, color)}\n\n")
        file_object.close()

    def write_h4(self, text="include_text", color=None):
        file_object = open(self.file_name, "a")
        file_object.write(f"#### {CustomMarkdown.apply_color(text, color)}\n\n")
        file_object.close()

    def write_codeblock(self, code="", language="", new_lines=1):
        file_object = open(self.file_name, "a")
        file_object.write(f"\n```{language}\n")
        file_object.write(f"{code}\n")
        file_object.write(f"```\n\n" + "\n" * new_lines)
        file_object.close()

    def write_text(self, text="include_text", bold=False, italic=False, new_lines=0, color=None):
        file_object = open(self.file_name, "a")
        appendix = ("*" if italic else "") + ("**" if bold else "")
        file_object.write(f"{appendix}{CustomMarkdown.apply_color(text, color)}{appendix}\n" + "\n" * new_lines)
        file_object.close()

    def write_encapsulated(self, text="include_text", color=None):
        file_object = open(self.file_name, "a")
        file_object.write(f"`{CustomMarkdown.apply_color(text, color)}`")
        file_object.close()

    def write_encapsulated(self, text="include_text", color=None):
        file_object = open(self.file_name, "a")
        file_object.write(f"`{CustomMarkdown.apply_color(text, color)}`")
        file_object.close()

    def write_horizontal_line(self):
        file_object = open(self.file_name, "a")
        file_object.write(f"\n\n\n---\n\n\n\n\n")
        file_object.close()


if __name__ == "__main__":
    pass
