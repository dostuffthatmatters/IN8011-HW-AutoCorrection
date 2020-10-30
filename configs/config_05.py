
config = {
    "HW_NUMBER": 5,

    # The file that the students were provided with
    "GIVEN_FILES": ["funct_lib.c", "funct_lib.h", "main_riemann_correction.c"],

    # The files that are required to be in the submitted zip-file
    "SUBMISSION_FILES": ["riemann.c", "riemann.h"],

    # These are alle the files that should be compiled and linked together.
    # May not be equal to GIVEN_FILES + SUBMISSION_FILES. However all files
    # from GIVEN_FILES + SUBMISSION_FILES will be present in the directory
    # where the compilation takes place
    "COMPILATION_FILES": ["main_riemann_correction.c", "riemann.c", "funct_lib.c"]
}
