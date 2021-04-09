#!/usr/bin/env python3

import re
import tkinter as tk
from tkinter import filedialog as fd 

class SqlKeywordsFormatterApp(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
    
    def initialize(self):
        self.filename = ""

        self.choose_file_button = tk.Button(text='Choose file', command = self.choose_file)
        self.choose_file_button.pack(pady=10)

        self.chosen_file = tk.Label(text = "Chosen file:")
        self.chosen_file.pack(pady=10)

        self.format_file_button = tk.Button(text='Format file', command = self.format_keywords)
        self.format_file_button.pack(pady=10)

        self.messages_label = tk.Label(text = '')
        self.messages_label.pack(pady=10)
 

    def choose_file(self):
        self.filename = fd.askopenfilename(filetypes=[('SQL File', '*.sql')])
        self.chosen_file.configure(text = "Chosen file:\n" + self.filename)

    def format_keywords(self):
        if self.filename == '':
            self.messages_label.configure(text = "You have to choose a file.")
            return
        

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
            with open(self.filename, 'r') as input_file:
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
            self.messages_label.configure(text = "ERROR: Could not open/read file")
            return

        # Close file explicitly
        input_file.close()

        try:
            with open(self.filename, 'w') as output_file:
                for line in lines:
                    output_file.write(line)
        except OSError:
            self.messages_label.configure("ERROR: Could not open/read file")
            return

        # Close file explicitly
        output_file.close()

        self.messages_label.configure(text = "Formatted " + self.filename + " successfully.")


if __name__ == "__main__":
    app = SqlKeywordsFormatterApp(None)
    app.title('SQL Keywords Formatter')
    app.geometry('700x200')
    app.mainloop()