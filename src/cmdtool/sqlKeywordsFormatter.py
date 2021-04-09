#!/usr/bin/env python3

import re
import sys
import argparse


# Takes a file as argument and changes all keywords to uppercase
# All other words will be changed to lowercase
def format_keywords(infile: str, outfile: str):
    if not infile.endswith('.sql'):
        print("The input file is not a sql file.")
        sys.exit(-1)
    elif not outfile.endswith('.sql'):
        print("The output file should also be a sql file.")
        sys.exit(-1)

    # List of SQL Keywords
    keywords = ['add', 'constraint', 'alter', 'all', 'and', 'any', 'as', 'asc', 'avg', 'backup',
                'between', 'by', 'case', 'check', 'column', 'constraint', 'count', 'create', 'database', 'default',
                'delete', 'desc', 'distinct', 'drop', 'exec', 'exists', 'foreign', 'from',
                'full', 'group', 'having', 'in', 'index', 'inner', 'insert', 'into',
                'is', 'join', 'key', 'left', 'like', 'limit', 'not', 'null', 'on', 'or',
                'order', 'outer', 'primary', 'procedure', 'right', 'rownum', 'select',
                'set', 'table', 'top', 'truncate', 'union', 'unique', 'update', 'values', 'view', 'where'
                ]

    # List to save the edited lines
    lines = []

    try:
        # Read from file and save lines in list
        with open(infile, 'r') as input_file:
            is_multiline_comment = False

            for line in input_file:
                # Detect multiline comments and don't edit them
                if line.startswith('/*') or line.startswith('*/'):
                    if is_multiline_comment:
                        is_multiline_comment = False
                    else:
                        is_multiline_comment = True

                # Only replace keywords if line isn't a comment
                if not line.startswith('--') and not is_multiline_comment and line != '\n':
                    line = line.lower()
                    for keyword in keywords:
                        line = re.sub(r"\b%s\b" % keyword, keyword.upper(), line)

                lines.append(line)
    except OSError:
        print("ERROR: Could not open/read file")
        sys.exit(-1)

    # Close file explicitly
    input_file.close()

    try:
        with open(outfile, 'w+') as output_file:
            for line in lines:
                output_file.write(line)
    except OSError:
        print("ERROR: Could not open/read file")
        sys.exit(-1)

    # Close file explicitly
    output_file.close()

    print('Formatted ' + infile + ' successfully to ' + outfile)


def main(args):
    # Check if output file was specified
    if args.o == None:
        format_keywords(args.File, args.File)
    else:
        format_keywords(args.File, args.o)


if __name__ == "__main__":
    # Use argument parser to provide arguments
    parser = argparse.ArgumentParser(description='Format Keywords in SQL Files')
    parser.add_argument('File', metavar='F', type=str, help='The file which should be formatted')
    parser.add_argument('-o', help='Specifiy output file for formatted SQL File. If not used the input file will be the output file.')
    args = parser.parse_args()

    main(args)
    