from PIL import Image, ImageDraw, ImageFont

import html

import os
from os.path import join

import pygments
import pygments.lexers as lexers
import pygments.formatters as formatters
import pygments.styles as styles

FONT_COLOR_INSTRUCTION = (200, 200, 200)
FONT_SIZE = 32

OUTPUT_DIRECTORY = 'output_images'


def create_image_from_code(language, function_name, code, code_task=""):
    print("creating image for " + function_name)
    full_size_x = 1280  # 1920
    full_size_y = 1024  # 1080
    image = Image.new('RGBA', (full_size_x, full_size_y), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    inconsolata = ImageFont.truetype('fonts/Inconsolata-Regular.ttf', FONT_SIZE)

    # draw instructions for code task
    (instruction_width, instruction_height) = ImageDraw.ImageDraw(image).textsize(text=code_task, font=inconsolata)
    draw.text((full_size_x / 2 - instruction_width / 2, (full_size_y / 20)), code_task, FONT_COLOR_INSTRUCTION, font=inconsolata)

    # draw code
    code_in_html = create_syntax_highlighting_html(language, code)
    code_in_html = html.unescape(code_in_html)
    code_in_html = code_in_html.replace('\t', '    ')
    code_in_html = code_in_html.replace('<span></span>', '')

    (allTextSizeX, allTextSizeY) = ImageDraw.ImageDraw(image).multiline_textsize(text=code, font=inconsolata)
    allTextSizeY *= 1.4  # for additional vertical padding, otherwise the text is too hard to read

    x_pos_start = (full_size_x / 2) - (allTextSizeX / 2)
    y_pos = (full_size_y / 2) - (allTextSizeY / 2)
    (nil, verticalPadding) = ImageDraw.ImageDraw(image).textsize(text='blubb', font=inconsolata)

    code_in_html_lines = code_in_html.split("\n")

    for code_line in code_in_html_lines:
        if code_line == '</pre></div>':
            break

        # remove four first characters from each line to offset the incorrect indentation
        if language == 'Java':
            if code_line.startswith('    '):
                code_line = code_line[4:]

        code_elements = code_line.split('<span')

        x_pos = x_pos_start
        y_pos += (verticalPadding * 1.4)

        for element in code_elements:
            element = element.replace('</span>', '')
            end_pos = element.find('>')

            span_class = ''

            if end_pos != -1:
                span_class = element[8:end_pos - 1]
                element = element[end_pos + 1:]

            draw.text((x_pos, y_pos), element, get_color_for_span_class(span_class), font=inconsolata)
            (sizeX, sizeY) = ImageDraw.ImageDraw(image).textsize(text=element, font=inconsolata)
            x_pos += sizeX

    write_image_to_file(function_name, image)


def write_image_to_file(file_name, image):
    if not os.path.isdir(OUTPUT_DIRECTORY):
        try:
            os.mkdir(OUTPUT_DIRECTORY)
        except Exception:
            print("Error creating the output repository")

    image.save(join(OUTPUT_DIRECTORY, file_name + '.png'), 'PNG')


def get_color_for_span_class(span_class):
    return {
        'kc': (0, 128, 0),
        'kd': (0, 0, 255),
        'k': (0, 128, 64),
        'kt': (67, 168, 237),
        'mi': (85, 26, 139),
        'nf': (102, 255, 255),
        'na': (125, 144, 41),
        'String': (125, 144, 41),
        'o': (102, 102, 102),
        's': (0, 128, 0),
        'sc': (0, 128, 0),
        'n': (255, 255, 255),
        'err': (255, 255, 255),
    }.get(span_class, (255, 255, 255))


def create_syntax_highlighting_html(language, code_function_string):
    # Create Pygments formatter (http://pygments.org/)
    formatter = formatters.get_formatter_by_name('html')
    formatter.full = True
    formatter.style = styles.get_style_by_name('manni')
    lexer = lexers.get_lexer_by_name(language)

    # Use pygments to create code with syntax highlighting in HTML
    code_in_html = pygments.highlight(code_function_string, lexer, formatter)

    # Convert syntax highlighting from HTML to the Presentation-format
    code_in_presentation = code_in_html
    pos = code_in_html.find('<pre>')
    code_in_presentation = code_in_presentation.replace(code_in_presentation[:pos + 5], '')

    return code_in_presentation
