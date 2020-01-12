
# Inside here you put all the files that have been provided for
# this homework -> The ones they didn't have to write by themselves,
# e.g. the testing "main"-file
GIVEN_DIRECTORY = "HW07/given"

# Inside here you put each submittees folder that you've downloaded
# from moodle -> In here are all the "..._assignsubmission_file_"-folders
SUBMISSION_DIRECTORY = "HW07/submission"



# The file that we provided them with
GIVEN_FILES = ["hanoi.h", "hanoi_solution.h", "hanoi_solution.c", "main_hanoi_correction.c"]

# The files that are required to be in the submitted zip-file
SUBMISSION_FILES = ["hanoi.c"]

# These are alle the files that should be compiled and linked together
# May not be equal to SUBMISSION_FILES + HOMEWORK_FILES
FILES_TO_COMPILE = ["main_hanoi_correction.c", "hanoi.c", "hanoi_solution.c"]



# Where should the resulting markdown file be put
PROTOCOL_LOCATION = "testing_protocol_hw07.md"
