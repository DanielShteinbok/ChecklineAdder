# Checkline Adder
At Infinite Potential Labs, the protocols used for CVD are written as csv files.
A problem that has been identified with the current setup is that if a protocol is started when the chamber pressure is too high,
the diffusion pump is exposed to too high a pressure.

An obvious solution is to simply add a line at the top of each protocol that checks whether the pressure is low enough before opening the angle valve to the diffusion pump
(closing the angle valve is generally safe, but opening it is generally not).

However, there are a whole bunch of legacy protocols to which this line must be added. This is tedious. I tried writing a VBA script to do this,
but I really hate VBA from the bottom of my heart and it was not easy to do so safely.

Python is better. Hence this project.

## Usage:
From the command line:

`python checkline_adder.py <path to directory with files>`

Only modifies CSV files in that directory.

Within python, to modify all csv files in a directory:

``` python
import checkline_adder

checkline_adder.eat_entire_directory("./path/to/directory")
```

again within python, to modify a single file:

``` python
import checkline_adder

checkline_adder.add_checkline_and_consecutive("./path/to/file.csv")
```

