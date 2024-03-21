### Hexlet tests and linter status:
[![Actions Status](https://github.com/Eugen980/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Eugen980/python-project-50/actions) 
[![Maintainability](https://api.codeclimate.com/v1/badges/389cedbb3a332ed67399/maintainability)](https://codeclimate.com/github/Eugen980/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/389cedbb3a332ed67399/test_coverage)](https://codeclimate.com/github/Eugen980/python-project-50/test_coverage)


### Differences generator 

The difference generator is a program that looks for differences between two files. Supports two types of files for definition - json and yaml. It has three types of output - stylish, plain, and json.

### Installation

Download the game and install from root directory 
To install the game from the repository,
use the command python3 -m pip install --user git+https://github.com/Eugen980/python-project-50.git

### Uninstallation

To delete it, use the command pip uninstall hexlet-code

### The work of the program

To output help, use the gendiff -h or --help command

To start the program, enter "gendiff" and the full paths for the files being compared
Example: gendiff ./tests/fixtures/file3.json ./tests/fixtures/file4.json

To select the output type, use the -f option with the format you need

Example: gendiff ./tests/fixtures/file3.json ./tests/fixtures/file4.json -f plain


### Demonstration of the work

[![asciicast](https://asciinema.org/a/Bde944UaasXjRr5eaHe8D4KK9.svg)](https://asciinema.org/a/Bde944UaasXjRr5eaHe8D4KK9)
