# gen-exe

[![GitHub workflow status: master](https://github.com/silvandeleemput/gen-exe/workflows/test-and-deploy/badge.svg?branch=master)](https://github.com/silvandeleemput/gen-exe/workflows)
[![PyPI version](https://badge.fury.io/py/gen-exe.svg)](https://badge.fury.io/py/gen-exe) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


A small utility which allows you to generate Windows executables that can run custom commands on your Windows system.

## Features

* generate portable executables that can run customizable commands
* commands can use the `{EXE_DIR}` macro to get the directory relative to the executable 
* the generated executable supports passing command-line arguments
* you can add icons during or after generation of the executable
* installation adds two CLIs: `gen-exe` and `add-icon-to-exe`

## Installation

Install from PyPi using:

`pip install gen-exe`

## Usage gen-exe

Custom commands can be embedded in the executables by providing a command string to the CLI, for example:

`gen-exe test.exe "echo hello world"`

The command string argument also supports the `{EXE_DIR}` macro, which expands the path where the
executable is executed from, for example:

`gen-exe test.exe "echo I am running from: {EXE_DIR}"`

This can be used to run relative executables:

`gen-exe test.exe "{EXE_DIR}\\another.exe"`

Optionally you can provide an icon file for the executable.

`gen-exe test.exe "echo I have a fancy icon now..." -i path-to-your.ico`

Another use case is to call a script or command using a Python interpreter, for example:

`gen-exe test.exe "python -c print(\'hello world\')"`

For other options see the help:

`gen-exe --help`

## Usage generated executables

Execute them by double clicking or via the command line:

`test.exe optional_argument_1 optional_argument_2`


## Usage add-icon-to-exe

To add an icon called `test.ico` to a `test.exe` executable file.

`add-icon-to-exe test.exe test.ico`

Note that the utility will replace any icons that already exist in the target executable.


## Contributing

Fork the gen-exe repository

Setup your forked repository locally as an editable installation:

```
$ cd ~
$ git clone https://github.com/yourproject/genexe
$ pip install --editable ./genexe
```

Now you can work locally and create your own pull requests.

Feel free to open issues and pull requests.

### Maintainer

Sil van de Leemput

### History

##### 0.2.1 (2021-02-08)

* Added hide-console option to the executable and the CLI

##### 0.2.0 (2021-02-07)

* Embedded runtimes in the executable. Executable should now work on Windows systems without VC++ redistributables installed 

##### 0.1.1 (2021-02-06)

* Better documentation - updated the README.md

##### 0.1.0 (2021-02-06)

* Initial release on PyPi
