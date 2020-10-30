
config = {
    "HW_NUMBER": 10,

    # The file that the students were provided with
    "GIVEN_FILES": ["main_sort_correction.c", "counting_sort.h"],

    # The files that are required to be in the submitted zip-file
    "SUBMISSION_FILES": ["counting_sort.c"],

    # These are alle the files that should be compiled and linked together.
    # May not be equal to GIVEN_FILES + SUBMISSION_FILES. However all files
    # from GIVEN_FILES + SUBMISSION_FILES will be present in the directory
    # where the compilation takes place
    "FILES_TO_COMPILE": ["main_sort_correction.c", "counting_sort.c"]
}
