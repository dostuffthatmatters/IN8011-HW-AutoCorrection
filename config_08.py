HW_NO = 8

# Inside here you put all the files that have been provided for
# this homework -> The ones they didn't have to write by themselves,
# e.g. the testing "main"-file
GIVEN_DIRECTORY = f"HW{'0' if HW_NO < 10 else ''}{HW_NO}/given"

# Inside here you put each submittees folder that you've downloaded
# from moodle -> In here are all the "..._assignsubmission_file_"-folders
SUBMISSION_DIRECTORY = f"HW{'0' if HW_NO < 10 else ''}{HW_NO}/submission"



# The file that we provided them with
GIVEN_FILES = ["main_list.c", "waiting_list.h"]

# The files that are required to be in the submitted zip-file
SUBMISSION_FILES = ["waiting_list.c"]

# These are alle the files that should be compiled and linked together
# May not be equal to SUBMISSION_FILES + HOMEWORK_FILES
FILES_TO_COMPILE = ["main_list.c", "waiting_list.c"]



# Where should the resulting markdown file be put
PROTOCOL_LOCATION = f"testing_protocol_hw{'0' if HW_NO < 10 else ''}{HW_NO}.md"
