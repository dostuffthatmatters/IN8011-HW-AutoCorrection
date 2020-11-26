
from src.utilities.custom_printer import CustomPrinter as cp


def test_custom_printing():
    for color in ['default', 'green', 'yellow', 'red', 'pink', 'blue']:
        for bold in [False, True]:
            for underline in [False, True]:
                cp.print(
                    f"print(color='{color}', bold='{bold}', underlime='{underline}')",
                    color=color, bold=bold, underline=underline, new_lines=2
                )

    cp.print_line(color='red')
    cp.print_line(bold=True)

    cp.print(
        {"param1": True, "param2": {"1": 1, "param3": [True, "now"]}}
    )
