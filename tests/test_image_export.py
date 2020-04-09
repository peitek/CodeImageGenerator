import os
import pytest

from codeimagegenerator import image_exporter
from tests.sample import sample_data


class TestImageExport:
    def test_image_export(self):
        # get sample data
        sample_name = 'ContainsSubstring'
        sample_content = sample_data.content_contains_substring

        # pass sample data to function
        image_exporter.create_image_from_code('Java', sample_name, sample_content)

        # assert image was created
        result_image = os.path.join(os.getcwd(), 'output_images', 'SC1_ContainsSubstring.png')
        assert os.path.exists(result_image) == 1
