
import os
from src.main import run_all_submission_tests
from configs.config_01 import config


def test_example_homework():
    assert('HW01' in os.listdir('.'))
    assert('given' in os.listdir('./HW01'))
    assert('submissions' in os.listdir('./HW01'))
    assert(len(os.listdir('./HW01/submissions')) == 4)

    assert('reports' in os.listdir('.'))

    run_all_submission_tests(config, print_results=False)

    assert('HW01' in os.listdir('.'))
    assert('given' in os.listdir('./HW01'))
    assert('submissions' in os.listdir('./HW01'))
    assert(len(os.listdir('./HW01/submissions')) == 4)

    assert('reports' in os.listdir('.'))
    assert('results_HW01.md' in os.listdir('./reports'))
