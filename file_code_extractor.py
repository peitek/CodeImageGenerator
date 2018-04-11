from os.path import join


code_function_start_lookups = ['public int ', 'public String ', 'public Integer ', 'public float ', 'public boolean ', 'public double[] ', 'public int[] ']


def convert_file(file_directory, file_name):
    with open(join(file_directory, file_name)) as text_file:
        code_file = text_file.read()

        # extract Java function from code file
        try:
            code_function_start, code_function_string, code_task = extract_function_from_file(code_file)
        except Exception:
            print("File could not extract a code function: ", file_name)
            return

        # get name of the function to specify the Presentation code block
        # TODO figure out unscrambled function name
        function_name_string = code_function_string[len(code_function_start):]
        function_name_position_end = function_name_string.find("(")
        function_name = function_name_string[:function_name_position_end]

        # remove FILE_SELECTION_SUBSTRINGS (LDBO, ..) from function name
        # TODO limit it to the function name to prevent bugs
        # TODO make this code more dynamic
        code_function_string = code_function_string \
            .replace('TD_B', '') \
            .replace('TD_N', '') \
            .replace('TD_U', '') \
            .replace('LDBO', '') \
            .replace('LDBS', '') \
            .replace('LOBO', '') \
            .replace('LOBS', '') \
            .replace('BU', '') \
            .replace('TD', '') \
            .replace('SY', '')

        return [function_name, code_function_string, code_task]


def extract_function_from_file(code_file):
    # TODO support multiple functions for each file
    code_function_start = next((x for x in code_function_start_lookups if x in code_file), False)

    if not code_function_start:
        raise Exception('no function found')

    code_task_position = code_file.find("[TASK]")

    if code_task_position != -1:
        code_task_string = code_file[code_task_position + 7:]
        code_task_end = code_task_string.find("\n")
        code_task_string = code_task_string[:code_task_end]
    else:
        code_task_string = ""

    code_function_position = code_file.find(code_function_start)
    code_function_string = code_file[code_function_position:]
    number_of_open_curly_brackets = 0
    code_function_end = -1
    for i, c in enumerate(code_function_string):
        if c == "{":
            number_of_open_curly_brackets += 1

        if c == "}":
            number_of_open_curly_brackets -= 1
            if (number_of_open_curly_brackets <= 0):
                code_function_end = i
                break
    code_function_string = code_function_string[:code_function_end + 1]
    return code_function_start, code_function_string, code_task_string