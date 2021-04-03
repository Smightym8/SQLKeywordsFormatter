import re
import sys


# Takes a file as argument and changes all keywords to uppercase
# All other words will be changed to lowercase
def format_keywords(file: str):
    if not file.endswith('.sql'):
        print("This file is not a sql file.")
        sys.exit(-1)

    # List of SQL Keywords
    keywords = ['add', 'constraint', 'alter', 'alter', 'all', 'and', 'any', 'as', 'asc', 'backup',
                'between', 'by', 'case', 'check', 'column', 'constraint', 'count', 'create', 'database', 'default',
                'delete', 'desc', 'distinct', 'drop', 'exec', 'exists', 'foreign', 'from',
                'full', 'group by', 'having', 'in', 'index', 'inner', 'insert into',
                'is null', 'is not null', 'join', 'key', 'left', 'like', 'limit', 'not', 'null', 'or',
                'order', 'outer', 'primary', 'procedure', 'right', 'rownum', 'select',
                'set', 'table', 'top', 'truncate', 'union', 'unique', 'update', 'values', 'view', 'where'
                ]

    # List to save the edited lines
    lines = []

    try:
        # Read from file and save lines in list
        with open(file, 'r') as input_file:
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
        with open(file, 'w') as output_file:
            for line in lines:
                output_file.write(line)
    except OSError:
        print("ERROR: Could not open/read file")
        sys.exit(-1)

    # Close file explicitly
    output_file.close()

    print("Formatted " + str(file) + " successfully.")


def usage():
    print("usage: python3 sqlKeywordsFormatter [Path to SQL File]")


def main(argv):
    if len(argv) != 1:
        usage()
    else:
        format_keywords(argv[0])


if __name__ == "__main__":
    main(sys.argv[1:])
