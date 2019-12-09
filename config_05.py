
# Inside here you put all the files that have been provided for
# this homework -> The ones they didn't have to write by themselves,
# e.g. the testing "main"-file
GIVEN_DIRECTORY = "HW05/given"

# Inside here you put each submittees folder that you've downloaded
# from moodle -> In here are all the "..._assignsubmission_file_"-folders
SUBMISSION_DIRECTORY = "HW05/submission"



# The file that we provided them with
GIVEN_FILES = ["funct_lib.c", "funct_lib.h", "main_riemann_correction.c"]

# The files that are required to be in the submitted zip-file
SUBMISSION_FILES = ["riemann.c", "riemann.h"]

# These are alle the files that should be compiled and linked together
# May not be equal to SUBMISSION_FILES + HOMEWORK_FILES
FILES_TO_COMPILE = ["main_riemann_correction.c", "riemann.c", "funct_lib.c"]



# Where should the resulting markdown file be put
PROTOCOL_LOCATION = "testing_protocol_hw05.md"
