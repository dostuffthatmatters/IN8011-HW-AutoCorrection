
from time import sleep
from src.utilities.custom_printing import CustomPrinting
from src.utilities.custom_markdown import CustomMarkdown


def print_report(results):
    sleep(0.05)
    for name in sorted(results.keys()):
        CustomPrinting.print_line(bold=True, character='-', new_lines=2)
        if results[name]["result"] == "Failed":
            CustomPrinting.print(f"{name} -> Failed:", color='red', bold=True)
            CustomPrinting.print_line(character='.')
            CustomPrinting.print(f"{results[name]['message']}")
            CustomPrinting.print_line(character='.', new_lines=2)
        else:
            CustomPrinting.print(
                f"{name} -> Successful until execution:",
                color='green', bold=True
            )
            CustomPrinting.print(f"\nOutput Stream:", bold=True)
            CustomPrinting.print_line(character='.')
            CustomPrinting.print(results[name]["output"])
            CustomPrinting.print_line(character='.', new_lines=2)

    CustomPrinting.print_line(bold=True, character='-')


def generate_md_report(results, hw_number):
    location = f"reports/report_HW{'0' if hw_number < 10 else ''}{hw_number}.md"
    markdown_object = CustomMarkdown(location)

    markdown_object.write_h2(
        f"Testing all submissions for Homework {hw_number}")
    markdown_object.write_text(
        text=f"{len(results)} submissions have been tested.",
        bold=True, new_lines=1
    )

    for name in sorted(results.keys()):
        markdown_object.write_horizontal_line()

        if results[name]["result"] == "Failed":
            markdown_object.write_h4(f"{name} -> Failed:", color=(255, 0, 0))
            markdown_object.write_codeblock(
                code=f"{results[name]['message']}", language="bash"
            )
            if "input" in results[name]:
                for input_file in results[name]["input"]:
                    markdown_object.write_text(
                        f"Input File `{input_file}`:", bold=True)
                    markdown_object.write_codeblock(
                        code=results[name]["input"][input_file], language="c", new_lines=0)
        else:
            markdown_object.write_h4(
                f"{name} -> Successful until execution:", color=(0, 200, 0))
            markdown_object.write_text(f"Output Stream:", bold=True)
            markdown_object.write_codeblock(
                code=results[name]["output"], language="bash")

            for input_file in results[name]["input"]:
                markdown_object.write_text(
                    f"Input File `{input_file}`:", bold=True)
                markdown_object.write_codeblock(
                    code=results[name]["input"][input_file], language="c", new_lines=0)
