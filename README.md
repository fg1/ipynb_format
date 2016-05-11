ipynb_format
============

`ipynb_format.py` is a small script to format the python code in ipython notebooks.
The code formatter is based on [`yapf`](https://github.com/google/yapf).


## Installation

On Linux:
```
$ pip install ipynb_format
```
or:
```
$ git clone https://github.com/fg1/ipynb_format.git
$ python setup.py install
```


## Usage

```
usage: ipynb_format [-h] [--style STYLE] [files [files ...]]

Format ipython notebook using yapf

positional arguments:
  files

  optional arguments:
    -h, --help     show this help message and exit
    --style STYLE  yapf style to use
```


The formatting style option is the same as for `yapf`.
