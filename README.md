# CodeImageGenerator

![Tests](https://github.com/peitek/CodeImageGenerator/workflows/Tests/badge.svg)

CodeImageGenerator is a Python script, which converts Java or Python files/functions to images. This includes a rough custom syntax highlighting with [Pygments](http://pygments.org/).

I personally use this to convert short code snippets for empirical research on program comprehension (see [Brains on Code](https://github.com/brains-on-code)).
This means the script is very personalized to my usage, and probably not directly useful to you without changes.

## Features

The main feature is to read all files from a directory, attempting to add syntax highlighting, and finally creating matching images.

Implemented so far:

* Reads all files from a directory, and parses one at a time
* Extracts just the function code from the file (and ignores the class, comments, etc around it)
* Uses Pygments to create syntax highlighting for the code
* Parses Pygments syntax highlighting to fit on the image
* Dynamically reduces font size if the code doesn't fit the screen
* Option to either strip boilerplate code and reduce to single method (or use full file)
* Rough support for Java and Python functions
* Rough image creation

## Limitations/Roadmap

Things I may add in the future:

* Better and cleaner (Python) code...
* Better configuration (in particular the output color scheme)
* Command line support
* Allow functions besides `public int`, `public String`, `public boolean`, and a couple of other static ones
* Only read Java files
* Support for more languages than just Java and Python


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
