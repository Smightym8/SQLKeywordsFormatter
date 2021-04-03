import re
import sys
import tkinter as tk
from tkinter import filedialog as fd 

# Takes a file as argument and changes all keywords to uppercase
# All other words will be changed to lowercase
def format_keywords(file: str):
    if not file.endswith('.sql'):
        messages_label.configure(text = "This file is not a sql file.")
        sys.exit(-1)

    # List of SQL Keywords
    keywords = ['add', 'constraint', 'alter', 'alter', 'all', 'and', 'any', 'as', 'asc', 'backup',
                'between', 'by', 'case', 'check', 'column', 'constraint', 'create', 'database', 'default',
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
        messages_label.configure(text = "ERROR: Could not open/read file")
        sys.exit(-1)

    # Close file explicitly
    input_file.close()

    try:
        with open(file, 'w') as output_file:
            for line in lines:
                output_file.write(line)
    except OSError:
        messages_label.configure(text = "ERROR: Could not open/read file")
        sys.exit(-1)

    # Close file explicitly
    output_file.close()

    messages_label.configure(text = "Formatted " + file + " successfully.")

def choose_file():
    filename = fd.askopenfilename(filetypes=[('SQL File', '*.sql')])
    chosen_file_label.configure(text = "Chosen file:\n" + filename)

    return filename

if __name__ == "__main__":
    #Window
    window = tk.Tk()
    window.title('SQL Keywords Formatter')
    window.geometry('600x200')

    file = ""

    #Widgets
    choose_file_button = tk.Button(text='Choose file', command = lambda: file == choose_file())
    choose_file_button.pack(pady=10)

    chosen_file_label = tk.Label(text = "Chosen file:")
    chosen_file_label.pack(pady=10)

    format_file_button = tk.Button(text='Format file')
    format_file_button.pack(pady=10)

    messages_label = tk.Label(text = '')
    messages_label.pack(pady=10)

    window.mainloop()