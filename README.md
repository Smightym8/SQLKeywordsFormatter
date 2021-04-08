# SQLKeywordsFormatter
<p> 
A commandline tool written in Python3 to format SQL Keywords to uppercase and other words to lowercase. This tool is for all who do not want to write keywords in uppercase themselves and prefer to simply write everything in small latters.
</p>

    usage: sqlKeywordsFormatter.py [-h] [-o O] F

    Format Keywords in SQL Files

    positional arguments:
        F           The file which should be formatted

    optional arguments:
        -h, --help  show this help message and exit
        -o O        Specifiy output file for formatted SQL File. If not used the input file will be the output file.
    
# Example
## Before using this tool
``` sql
select * 
from mytable;
```

## After using this tool
``` sql
SELECT *
FROM mytable;
```
