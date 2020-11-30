
import os
import re
from src.main import Main
from configs.config_01 import config


def test_reporting():
    if 'results_HW01.md' not in os.listdir('./reports'):
        Main.run(config)
    assert('results_HW01.md' in os.listdir('./reports'))

    report = open(
        f"./reports/results_HW01.md", 'r',
        encoding='utf-8'
    ).read()

    assert(len(re.findall("6 submissions have been tested", report)) == 1)

    assert(len(re.findall(".*Successful execution \(exit code 0\)", report)) == 3)
    assert(len(re.findall("<span style='color: rgb\(0, 200, 0\)'>.*", report)) == 3)

    assert(len(re.findall("<span style='color: rgb\(255, 0, 0\)'>.*", report)) == 3)

    assert(len(re.findall("(```c)([^`]+)(```)", report)) == 4), \
        "Invalid report format (c blocks missing)"
    assert(len(re.findall("(```c)([^`]{20,})(```)", report)) == 4), \
        "File reading stream empty"

    assert(len(re.findall("(```bash)([^`]+)(```)", report)) == 6), \
        "Invalid report format (bash blocks missing)"
    assert(len(re.findall("(```bash)([^`]{20,})(```)", report)) == 6), \
        "Output stream empty"
