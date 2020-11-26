
import os
from src.main import Main
from configs.config_01 import config


def test_example_homework():
    assert('HW01' in os.listdir('.'))
    assert('given' in os.listdir('./HW01'))
    assert('submissions' in os.listdir('./HW01'))
    assert(len(os.listdir('./HW01/submissions')) >= 6)

    assert('reports' in os.listdir('.'))

    Main.run(config)

    assert('HW01' in os.listdir('.'))
    assert('given' in os.listdir('./HW01'))
    assert('submissions' in os.listdir('./HW01'))
    assert(len(os.listdir('./HW01/submissions')) == 6)

    assert('reports' in os.listdir('.'))
    assert('results_HW01.md' in os.listdir('./reports'))
