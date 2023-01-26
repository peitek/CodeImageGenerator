import os
from os.path import isfile, join

from codeimagegenerator.file_code_extractor import convert_file
from codeimagegenerator import image_exporter

PROJECT_DIRECTORY = "C:/Users/norma/Documents/Research/CodeImageGenerator/" # TODO change to your setup
CODE_FILE_DIRECTORY = "tests/sample"
CODE_LANGUAGE = 'Java'
STRIP_BOILERPLATE_CODE = False

# if only specific files should be selected based on their (sub)-names, set this to True and customize FILE_SELECTION_SUBSTRINGS
LIMIT_TO_FILES_WITH_PARTICULAR_SUBSTRING = False
FILE_SELECTION_SUBSTRINGS = ['Contains']


def main():
    # TODO let this program be executable from the command line
    working_directory = join(PROJECT_DIRECTORY, CODE_FILE_DIRECTORY)
    print('checking directory', working_directory)

    # read all files from a directory and loop through them
    only_files = [f for f in os.listdir(working_directory) if isfile(join(working_directory, f))]

    for file_name in only_files:
        print('checking file', file_name)

        if LIMIT_TO_FILES_WITH_PARTICULAR_SUBSTRING:
            # only select files with a particular string in their name
            if any(x in file_name for x in FILE_SELECTION_SUBSTRINGS):
                [function_name, code_function_string, code_task] = convert_file(working_directory, CODE_LANGUAGE, STRIP_BOILERPLATE_CODE, file_name)
                image_exporter.create_image_from_code(CODE_LANGUAGE, function_name, code_function_string, code_task)
        else:
            [function_name, code_function_string, code_task] = convert_file(working_directory, CODE_LANGUAGE, STRIP_BOILERPLATE_CODE, file_name)
            image_exporter.create_image_from_code(CODE_LANGUAGE, function_name, code_function_string, code_task)


# Just call main function at the moment
if __name__ == '__main__':
    main()
