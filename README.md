# Overview

The intention of this program is to demonstrate the usefulness and versatility of the sqlite3 library built into Python. Specifically the ability to access, update, and query data from a database (`.db` file) held within any given folder or repository in order to more efficiently filter and retrieve data.

This personal project of mine has served its purpose of being a proof of concept that a perfect internet connection, nor other 3rd party software such as MySQL Workbench is neccessary to perform the same functions on a lighter IDE such as VS Code.

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

The relational database being used here is a generic `.db` file containing song, invoice, and employee tables and their relations with one another; according to their corresponding keys. 

The structure of the tables used in this program will only make use of the `albums` and `artists` tablesl for now. They will be created by the CREATE SQL keyword and subsequently populated by all available columns with their data. 3 columns from `albums` and 2 from `artists` related to eachother through the `ArtsistId` key.

# Development Environment

Developed on Visual Studio Code Version 1.63

Developed with Python 3.9.2

# Useful Websites


* [Sqlite 3 Python Tutorial in 5 minutes - Creating Database, Tables and Querying
](https://www.youtube.com/watch?v=girsuXz0yA8)
* [W3 Schools SQL Tutorial](https://www.w3schools.com/sql/)
* [SQLite Tutorial](https://www.sqlitetutorial.net/)

# Future Work

Additional SQL functions will be added in order to further streamline the query process

* Streamline the Add and Update options
* Add a search option
