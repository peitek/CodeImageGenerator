import os
import pytest

from codeimagegenerator import file_code_extractor
from tests.sample import sample_data


class TestCodeExtractor:
    def test_code_extractor_contains_substring(self):
        [function_name, code_function_string, code_task] = file_code_extractor.convert_file(os.path.join(os.getcwd(), 'tests/sample'), 'Java', False, 'ContainsSubstring.java')

        assert function_name == 'ContainsSubstring'
        assert code_function_string == sample_data.content_contains_substring
        assert code_task == ''

    def test_code_extractor_array_average(self):
        [function_name, code_function_string, code_task] = file_code_extractor.convert_file(os.path.join(os.getcwd(), 'tests/sample'), 'Java', False, 'ArrayAverage.java')

        assert function_name == 'ArrayAverage'
        assert code_function_string == sample_data.content_average_substring
        assert code_task == ''
