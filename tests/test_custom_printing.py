
from src.utilities.custom_printing import CustomPrinting


def test_custom_printing():
    for color in ['default', 'green', 'yellow', 'red', 'pink', 'blue']:
        for bold in [False, True]:
            for underline in [False, True]:
                CustomPrinting.print(
                    f"print(color='{color}', bold='{bold}', underlime='{underline}')",
                    color=color, bold=bold, underline=underline, new_lines=2
                )

    CustomPrinting.print_line(color='red')
    CustomPrinting.print_line(bold=True)

    CustomPrinting.print_dict(
        {"param1": True, "param2": {"1": 1, "param3": [True, "now"]}}
    )
