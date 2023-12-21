# How to Use

This code has been written using Python 3.

To use this program, all the .py files must be in the same folder.

## Prerequisites

In order for this program to work, the python module 'matplotlib' must be installed on your machine.

To install it on a linux distribution, first make sure pip is installed:

```commandline
sudo apt-get update
```

```commandline
sudo apt-get install pip
```

And then use pip to download matplotlib:

```commandline
sudo pip install matplotlib
```

## Execution

Open a terminal in the folder containing all the .py files and type the following command:

```commandline
python ./main.py [-n] <--alpha> [--attempts] [--output]  
```

Use the '-h/--help' flag to get a description of each arguments.

Example:

```commandline
python ./main.py -n 1000 -a 0.2 0.3 1/e 0.4 0.6 --attempts 100000 -o chart.png
```

