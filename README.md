# Interactive-Python-Dictionary

An interactive, command line dictionary made using Python.
  Input a word in the command line and the script returns you the meaning(s) for the given word.
  A smart feature to suggest close matches of the word is also included, in case of any mistype.

There are two Python scripts:
1. "InteractiveDictionary_App1.py" - In this script, the data source for the dictionary is "data.json" file.
2. "InteractiveDictionary_App2.py" - This script fetches the data from a remote MySQL database.
  To use this script, MySQL Connector for Python needs to be installed in the local system which can be downloaded from https://dev.mysql.com/downloads/connector/python/ depending on the Operating System of the local machine.
  To run the script without installing the MySQL Connector, Python's in-built 'sqlite3' package can be used for which the script can be modified accordingly by referencing the official documentation (https://docs.python.org/3/library/sqlite3.html).

To use the app:
- place the python script .json file in the same directory.
- open command prompt/terminal in the same directory and run the InteractiveDictionary_App1.py/InteractiveDictionary_App2.py script from terminal.
