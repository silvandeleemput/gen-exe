A small utility which allows you to generate Windows executables that can run custom commands on your Windows system.

Custom commands can be embedded in the executables by providing a command string to the CLI, for example:

`gen-exe ./test.exe "echo hello world"`

The command string argument also supports the `{EXE_DIR}` macro, which expands the path where the
executable is executed from, for example:

`gen-exe ./test.exe "echo I am running from: {EXE_DIR}"`

This can be used to run relative executables:

`gen-exe ./test.exe "{EXE_DIR}\\another.exe"`

Optionally you can provide an icon file for the executable.

`gen-exe ./test.exe "echo I have a fancy icon now..." -i ./path-to-your.ico`

Another use case is to call a script or command using a Python interpreter, for example:

`gen-exe ./test.exe "python -c print(\'hello world\')"`

For other options see the help:

`gen-exe --help`

### Installation

Install from PyPi using:

`pip install gen-exe`

### Contributing

Fork the solitude repository

Setup your forked repository locally as an editable installation:

```
$ cd ~
$ git clone https://github.com/yourproject/genexe
$ pip install --editable ./genexe
```

Now you can work locally and create your own pull requests.

#### Maintainer

Sil van de Leemput

#### History

##### 0.0.1 (2021-02-06)

* Initial release on PyPi
