### Bank Account Simulation
Video Demo:  <https://youtu.be/v_8ZWQGxZN0>
## Description:
# Table of Content
- requirements
- Installation
- project
- test_project

# Table of included files
- requirements.txt --> This file includes all the required libraries to run the application
- clients.csv --> This file contains all the data of all the clients registered in the bank, including their (id, first name, last name, email, and balance) in order
- project.py --> This file includes all the execution of all functions and classes
- test_project.py --> This file is used to unit test some of the functions in the project using pytest
- README.md

# Requirements:
This module requires the following modules:
- pandas (https://pandas.pydata.org/)
- tabulate (https://pypi.org/project/tabulate/)

# Installation
Install as you would normally install a normal module. For further information, see:
1- [https://pandas.pydata.org/getting_started.html]
2- [https://pypi.org/project/tabulate/]

## Project
# Course
CS50P, Harvard's CS50's Introduction to Programming with Python.
# Purpose
This project was made for the purpose of applying all the skills acquired from CS50P and putting them into practice.
# Overview
This project was developed using only python.
# Important Functions:
- read_file(): Reads the file containing clients' data by opening the file containing clients' data then looping through the file and append data to the clients stack then returning it
- get_data(client_data): Gets the a certain client's data by looping forever untill the user inputs a valid name or (Control-d), inside that loop, the program loops through all the client names untill you find the client then return the data
- options(): Displays options of what the client can do and returns his choice
- operation(choice): Decides which operation will be done on depending on the user's input
- print_statement(id, first, last, email, balance, date): Display a table containing all the user's data, (id, first name, last name, email, balance, time when the statement was printed)
- update_balance(id, new_balance): Reads the CSV file and set the index to the "ID" column, then updates a cell based on the index (ID) and column then writes the changes into the file.
