from PIL import Image, ImageDraw, ImageFont

import html

import os
from os.path import join

import pygments
import pygments.lexers as lexers
import pygments.formatters as formatters
import pygments.styles as styles

FONT_COLOR_INSTRUCTION = (220, 220, 220)

FONT_SIZE_INSTRUCTION = 38
FONT_SIZE_CODE = 44

DEFAULT_VERTICAL_PADDING = 1.6
MINIMUM_VERTICAL_PADDING = 1.05

REMOVE_DEFAULT_INDENTATION = False

IMAGE_SIZE_X = 1280  # 1920
IMAGE_SIZE_Y = 1024  # 1080

OUTPUT_DIRECTORY = 'output_images'


def create_image_from_code(language, function_name, code, code_task=""):
    print("creating image for " + function_name)

    image = Image.new('RGBA', (IMAGE_SIZE_X, IMAGE_SIZE_Y), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    # draw instructions for code task after figuring out fitting font size
    font_size_instruction = FONT_SIZE_INSTRUCTION
    while True:
        inconsolata_instructions = ImageFont.truetype('fonts/Inconsolata-Regular.ttf', font_size_instruction)

        (instruction_width, instruction_height) = ImageDraw.ImageDraw(image).textsize(text=code_task, font=inconsolata_instructions)

        if instruction_width > 0.95*IMAGE_SIZE_X:
            print('-> Too much instruction text to horizontally fit on the configured image size -> trying a smaller font')

            font_size_instruction -= 1
        else:
            break

    draw.text((IMAGE_SIZE_X / 2 - instruction_width / 2, (IMAGE_SIZE_Y / 30)), code_task, FONT_COLOR_INSTRUCTION, font=inconsolata_instructions)

    # draw code
    code_in_html = create_syntax_highlighting_html(language, code)
    code_in_html = html.unescape(code_in_html)
    code_in_html = code_in_html.replace('\t', '    ')
    code_in_html = code_in_html.replace('<span></span>', '')

    font_size = FONT_SIZE_CODE
    additional_vertical_padding = DEFAULT_VERTICAL_PADDING
    while True:
        inconsolata = ImageFont.truetype('fonts/Inconsolata-Regular.ttf', font_size)

        (allTextSizeX, allTextSizeY) = ImageDraw.ImageDraw(image).multiline_textsize(text=code, font=inconsolata)
        allTextSizeY *= additional_vertical_padding  # for additional vertical padding, otherwise the text is too hard to read

        if allTextSizeX > 0.95*IMAGE_SIZE_X:
            print('-> Too much code text to horizontally fit on the configured image size -> trying a smaller font')

            font_size -= 1
        elif allTextSizeY > 0.85 * (IMAGE_SIZE_Y - instruction_height):
            print('-> Too much code text to vertically fit on the configured image size -> trying a smaller font and less padding')

            font_size -= 1
            if additional_vertical_padding > MINIMUM_VERTICAL_PADDING:
                additional_vertical_padding -= 0.08
        else:
            break

    (nil, height_of_font) = ImageDraw.ImageDraw(image).textsize(text='placeholder text', font=inconsolata)

    x_pos_start = (IMAGE_SIZE_X / 2) - (allTextSizeX / 2)
    y_pos = (IMAGE_SIZE_Y / 2) - (allTextSizeY / 2) - height_of_font

    code_in_html_lines = code_in_html.split("\n")

    for code_line in code_in_html_lines:
        if code_line == '</pre></div>':
            break

        # remove four first characters from each line to offset the incorrect indentation
        if REMOVE_DEFAULT_INDENTATION:
            if language == 'Java':
                if code_line.startswith('    '):
                    code_line = code_line[4:]

        code_elements = code_line.split('<span')

        x_pos = x_pos_start
        y_pos += (height_of_font * additional_vertical_padding)

        for element in code_elements:
            element = element.replace('</span>', '')
            end_pos = element.find('>')

            span_class = ''

            if end_pos != -1:
                span_class = element[8:end_pos - 1]
                element = element[end_pos + 1:]

            draw.text((x_pos, y_pos), element, get_color_for_span_class(element, span_class), font=inconsolata)
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


def get_color_for_span_class(element, span_class):
    # some exception cases:
    if element.rstrip() == 'sum' or element.rstrip() == 'input' or element.rstrip() == 'reversed':
        return 255, 255, 255
    elif element.rstrip() == 'in' or \
         element.rstrip() == 'range' or \
         element.rstrip() == 'len' or \
         element.rstrip() == 'math':
        return 67, 168, 237

    return {
        'kc': (0, 128, 0),
        'kd': (0, 0, 255),
        'k': (50, 178, 114),  # python keywords: def, return, if
        'kt': (67, 168, 237),
        'mi': (155, 96, 209), # numbers
        'n': (255, 255, 255),  # regular source code text
        'nb': (50, 178, 114), # python: "len" operator
        'nf': (122, 255, 255),
        'na': (125, 144, 41),
        'String': (125, 144, 41),
        'o': (125, 125, 125), # (assignment) operators
        'ow': (50, 178, 114), # python: "in" operator
        'p': (220, 220, 220), # python: [] characters
        's': (0, 128, 0),
        'sc': (0, 128, 0),
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
