
config = {
    "HW_NUMBER": 6,

    # The file that the students were provided with
    "GIVEN_FILES": ["swap.h", "main_swap_correction.c"],

    # The files that are required to be in the submitted zip-file
    "SUBMISSION_FILES": ["swap.c"],

    # These are alle the files that should be compiled and linked together.
    # May not be equal to GIVEN_FILES + SUBMISSION_FILES. However all files
    # from GIVEN_FILES + SUBMISSION_FILES will be present in the directory
    # where the compilation takes place
    "FILES_TO_COMPILE": ["main_swap_correction.c", "swap.c"]
}
