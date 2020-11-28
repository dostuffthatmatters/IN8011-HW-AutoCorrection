
from time import sleep
from src.utilities.custom_printer import CustomPrinter as cp
from src.utilities.custom_markdown import CustomMarkdown as cm


class Reporting:

    @staticmethod
    def print(results):
        sleep(0.05)
        for name in sorted(results.keys()):
            cp.print_line(bold=True, character='-', new_lines=2)
            if results[name]["result"] == "Failed":
                cp.print(f"{name} -> Failed:", color='red', bold=True)
                cp.print_line(character='.')
                cp.print(f"{results[name]['message']}")
                cp.print_line(character='.', new_lines=2)
            else:
                cp.print(
                    f"{name} -> Successful until execution:",
                    color='green', bold=True
                )
                cp.print(f"\nOutput Stream:", bold=True)
                cp.print_line(character='.')
                cp.print(results[name]["output"])
                cp.print_line(character='.', new_lines=2)

        cp.print_line(bold=True, character='-')

    @staticmethod
    def generate_markdown(results, hw_number):
        location = f"reports/results_HW{'0' if hw_number < 10 else ''}{hw_number}.md"
        md = cm(location)

        md.write_heading(
            f"Testing all submissions for Homework {hw_number}",
            heading_type='h2'
        )
        md.write_text(
            text=f"{len(results)} submissions have been tested.",
            bold=True, new_lines=1
        )

        for name in sorted(results.keys()):

            md.write_horizontal_line()

            if results[name]["result"] == "Failed":
                md.write_heading(
                    f"{name} -> Failed:", color=(255, 0, 0),
                    heading_type='h3'
                )
                md.write_codeblock(
                    code=f"{results[name]['message']}", language="bash"
                )
                if "input" in results[name]:
                    for input_file in results[name]["input"]:
                        md.write_text(
                            f"Input File `{input_file}`:", bold=True)
                        md.write_codeblock(
                            code=results[name]["input"][input_file], language="c", new_lines=0)
            else:
                md.write_heading(
                    f"{name} -> Successful until execution:", color=(0, 200, 0),
                    heading_type='h3'
                )
                md.write_text(f"Output Stream:", bold=True)
                md.write_codeblock(
                    code=results[name]["output"], language="bash")

                for input_file in results[name]["input"]:
                    md.write_text(
                        f"Input File `{input_file}`:", bold=True)
                    md.write_codeblock(
                        code=results[name]["input"][input_file], language="c", new_lines=0)
