#!/usr/bin/env python
#import csv
#
import os
import sys

def add_checkline_and_consecutive(filename):
    """
    if a file already has the line that checks for pressure, does not add it.
    Otherwise, adds a line that checks the pressure before starting the rest of the protocol.
    Afterwards, proceeds to redo the numbering of the steps such that they are consecutive.
    """
    # add the checkline, which checks that pressure is sufficiently low before beginning the rest of the protocol
    # note: the protocol files use \r\n at end of each line
    checkline =  "1,5,Check pressure below A3@10-3,TRUE,0,20,TRUE,0,0,90,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,TRUE,0,FALSE,0,FALSE,FALSE,FALSE,0,FALSE,FALSE,FALSE,0,FALSE,FALSE,FALSE,0,FALSE,FALSE,FALSE,0,FALSE,FALSE,FALSE,0,FALSE,FALSE,FALSE,0,FALSE,FALSE,FALSE,0,FALSE,FALSE,0.05,0.001\r\n"
    file_contents = []
    with open(filename, 'r', newline='\r\n', encoding="iso-8859-1") as file:
        file_contents.append(file.readline())
        second_line = file.readline()
        #if second_line.split(",")[2] != "Check pressure below A3@10-3":
        current_number = 2
        if second_line != checkline:
            file_contents.append(checkline)
            elements = second_line.split(",")
            elements[0] = current_number
            for index in range(len(elements)):
                elements[index] = str(elements[index])
            #file_contents.append(elements.join(","))
            file_contents.append(",".join(elements))
            current_number += 1
        else:
            file_contents.append(checkline)
        for line in file:
            elements = line.split(",")
            # TODO: check whether the first element in the line is empty. If so, ignore the line
            elements[0] = current_number
            for index in range(len(elements)):
                elements[index] = str(elements[index])
            #file_contents.append(elements.join(","))
            file_contents.append(",".join(elements))
            current_number += 1
    with open(filename, 'w', encoding="iso-8859-1") as file:
        file.write("".join(file_contents))
    #print(repr("".join(file_contents)))

def eat_entire_directory(directory):
        """
        apply add_checkline_and_consecutive to each csv file in a given directory
        """
        #os.chdir(sys.argv[1])
        os.chdir(directory)
        filenames = os.listdir()
        # select only files with a csv file extension
        only_csvs = [filename for filename in filenames if filename.split(".")[-1] == "csv"]
        for filename in only_csvs:
            print("processing: " + filename)
            add_checkline_and_consecutive(filename)

if __name__ == "__main__":
    eat_entire_directory(sys.argv[1])
