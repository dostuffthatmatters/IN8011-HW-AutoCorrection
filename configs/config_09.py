
config = {
    "HW_NUMBER": 9,

    # The file that the students were provided with
    "GIVEN_FILES": ["main_tree.c", "sorted_tree.h"],

    # The files that are required to be in the submitted zip-file
    "SUBMISSION_FILES": ["sorted_tree.c"],

    # These are alle the files that should be compiled and linked together.
    # May not be equal to GIVEN_FILES + SUBMISSION_FILES. However all files
    # from GIVEN_FILES + SUBMISSION_FILES will be present in the directory
    # where the compilation takes place
    "COMPILATION_FILES": ["main_tree.c", "sorted_tree.c"]
}
