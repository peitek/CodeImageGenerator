import os
from os.path import isfile, join

from file_code_extractor import convert_file
import image_exporter

# TODO make config accessible from outside
# config

CODE_FILE_DIRECTORY = "C:/Users/npeitek/Documents/fmri-code-complexity/complexity-snippets/src/progcode4"

#CODE_FILE_DIRECTORY = "C:/Users/npeitek/Documents/fmri-td/CodeSnippets/java/src/com/fmri/topdown/original/number"
#CODE_FILE_DIRECTORY = "C:/Users/npeitek/Documents/fmri-td/CodeSnippets/java/src/com/fmri/topdown/original/words"
#CODE_FILE_DIRECTORY = "C:/Users/npeitek/Documents/fmri-td/CodeSnippets/java/src/com/fmri/topdown/original/syntax"
CODE_LANGUAGE = 'Java'

#CODE_FILE_DIRECTORY = "C:/Users/npeitek/Documents/fmri-td/CodeSnippets/python/words"
#CODE_LANGUAGE = 'Python'

STRIP_BOILERPLATE_CODE = False

# if only specific files should be selected based on their (sub)-names, set this to True and customize FILE_SELECTION_SUBSTRINGS
LIMIT_TO_FILES_WITH_PARTICULAR_SUBSTRING = False
FILE_SELECTION_SUBSTRINGS = ['BU', 'LOBO', 'LOBS']


def main():
    # TODO let this program be executable from the command line
    # read all files from a directory and loop through them
    only_files = [f for f in os.listdir(CODE_FILE_DIRECTORY) if isfile(join(CODE_FILE_DIRECTORY, f))]

    for file_name in only_files:
        if LIMIT_TO_FILES_WITH_PARTICULAR_SUBSTRING:
            # only select files with a particular string in their name
            if any(x in file_name for x in FILE_SELECTION_SUBSTRINGS):
                [function_name, code_function_string, code_task] = convert_file(CODE_FILE_DIRECTORY, CODE_LANGUAGE, file_name)
                image_exporter.create_image_from_code(function_name, code_function_string, code_task)
        else:
            [function_name, code_function_string, code_task] = convert_file(CODE_FILE_DIRECTORY, CODE_LANGUAGE, STRIP_BOILERPLATE_CODE, file_name)
            image_exporter.create_image_from_code(CODE_LANGUAGE, function_name, code_function_string, code_task)


# Just call main function at the moment
main()
