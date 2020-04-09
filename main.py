import os
from os.path import isfile, join

from codeimagegenerator.file_code_extractor import convert_file
from codeimagegenerator import image_exporter

# TODO make config accessible from outside
# config

CODE_FILE_DIRECTORY = "C:/Users/Norman/Documents/Research/fmri-study-code-complexity-metrics/complexity-snippets/src/progcode5_prestudy"
CODE_LANGUAGE = 'Java'
STRIP_BOILERPLATE_CODE = False

# if only specific files should be selected based on their (sub)-names, set this to True and customize FILE_SELECTION_SUBSTRINGS
LIMIT_TO_FILES_WITH_PARTICULAR_SUBSTRING = False
FILE_SELECTION_SUBSTRINGS = ['Contains']


def main():
    # TODO let this program be executable from the command line
    # read all files from a directory and loop through them
    only_files = [f for f in os.listdir(CODE_FILE_DIRECTORY) if isfile(join(CODE_FILE_DIRECTORY, f))]

    for file_name in only_files:
        if LIMIT_TO_FILES_WITH_PARTICULAR_SUBSTRING:
            # only select files with a particular string in their name
            if any(x in file_name for x in FILE_SELECTION_SUBSTRINGS):
                [function_name, code_function_string, code_task] = convert_file(CODE_FILE_DIRECTORY, CODE_LANGUAGE, STRIP_BOILERPLATE_CODE, file_name)
                image_exporter.create_image_from_code(CODE_LANGUAGE, function_name, code_function_string, code_task)
        else:
            [function_name, code_function_string, code_task] = convert_file(CODE_FILE_DIRECTORY, CODE_LANGUAGE, STRIP_BOILERPLATE_CODE, file_name)
            image_exporter.create_image_from_code(CODE_LANGUAGE, function_name, code_function_string, code_task)


# Just call main function at the moment
if __name__ == '__main__':
    main()
