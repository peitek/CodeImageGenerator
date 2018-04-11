# CodeImageGenerator

CodeImageGenerator is a Python script, which converts Java files/functions to images. This includes a rough custom syntax highlighting with [Pygments](http://pygments.org/).

I personally use this to convert short code snippets for empirical research on program comprehension (see [Brains on Code](https://github.com/brains-on-code)).
This means the script is very personalized to my usage, and probably not directly useful to you without changes.

**Disclaimer: I am not a Python programmer. I'm always grateful for feedback on how to improve my code.**

## Features

The main feature is to read all files from a directory, attempting to add syntax highlighting, and finally creating matching images.

Implemented so far:

* Reads all files from a directory, and parses one at a time
* Extracts just the function code from the file (and ignores the class, comments, etc around it)
* Uses Pygments to create syntax highlighting for the code
* Parses Pygments syntax highlighting to a Presentation-compatible format
* Rough image creation

## Roadmap

Things I may add in the future:

* Better and cleaner (Python) code...
* Better configuration (in particular the output color scheme)
* Warnings when code doesn't fit on screen
* Command line support
* Allow multiple functions per file
* Allow functions besides `public int`, `public String`, `public boolean`, and a couple of other static ones
* Only read Java files
* Support for more languages than just Java


## Font

The text is generated with the Inconsolata font. The font licence is here: [Inconsolata licence](https://www.fontsquirrel.com/license/Inconsolata).


## Setup ##

The project should run in any Python environment. It was developed and tested with [PyCharms](https://www.jetbrains.com/pycharm/).

# Contributing #

Do you want to fix my horrible Python code? Feel free to create a pull request :)

Thank you!


# License #

```
MIT License

Copyright (c) 2018 Norman Peitek
```