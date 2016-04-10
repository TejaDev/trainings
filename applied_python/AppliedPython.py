
# coding: utf-8

# In[ ]:

import datetime                                                                                       

day_today = datetime.date.today().strftime("%A")
print "Today is {day}".format(day=day_today)


# In[ ]:

if day_today is "Friday":
    print "Today is Friday!!"
else:
    print "Today is {day}".format(day=day_today)


# In[ ]:

# # multiply each number by 2

numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    print number ** 2


# In[ ]:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# numbers = range(1, 11)

for number in numbers:
    if number % 2 == 0:
        print "Number {} is even".format(number)
    elif number % 2 == 1:
        print "Number {} is odd".format(number)
    else:
        print "is it number: {}?".format(number)


# In[ ]:

# List comprehension

even_numbers = [number for number in range(1,11) if number % 2 == 0]
print "Even numbers: ", even_numbers

odd_numbers = [number for number in range(1,11) if number % 2 == 1]
print "Odd numbers:", odd_numbers


# In[ ]:

numbers = range(1, 30)
even_numbers = [number for number in range(1,11) if number % 2 == 0]

even_numbers = set(even_numbers)
numbers = set(numbers)

# difference (-) -> new set with elements in numbers but not in even_numbers
# so we can get odd_numbers

odd_numbers = list(numbers - even_numbers)
print "Odd numbers: ", odd_numbers


# In[ ]:

while True:
    number = input("Please provide number: ")
    if number % 2 == 0:
        print "Number {} is even".format(number)
    elif number % 2 == 1:
        print "Number {} is odd".format(number)
    else:
        print "is it number: {}?".format(number)
    break


# In[ ]:

def is_number_even(number):
    if number % 2 == 0:
        print "Number {} is even".format(number)
        return True
    elif number % 2 == 1:
        print "Number {} is odd".format(number)
    else:
        print "is it number: {}?".format(number)
    return False


while True:
    number = input("Please provide number: ")
    is_number_even(number)
    break


# In[ ]:

while True:
    number = input("Please provide number: ")
    try:
        number = int(number)
    except ValueError as exc:
        print "Do we have number or not?"
        break
    is_number_even(number)
    break


# In[ ]:

# very, very, very ... simple calc

def add_numbers(n1, n2):
    return n1 + n2

def multiply_numbers(n1, n2):
    return n1 * n2

def subtract_numbers(n1, n2):
    return n1 - n2

def divide_numbers(n1, n2):
    return n1 / n2

actions = {
        'add': add_numbers,
        'multiply': multiply_numbers,
        'subtract': subtract_numbers,
        'divide': divide_numbers,
}

action = raw_input("Choose one action [add|multiply|subtract|divide|]:")
number1 = raw_input("Provide first number: ")
number2 = raw_input("Provide second number: ")

# convert to int
number1 = int(number1)
number2 = int(number2)

print "You will {action} two numbers {number1} and {number2}".format(**locals())
result = actions[action](number1, number2)
print "Result is: ", result


# In[ ]:

class SimpleCalc(object):
    def __init__(self, number1, number2):
        self.n1 = number1
        self.n2 = number2

    def add(self):
        return self.n1 + self.n2

    def multiply(self):
        return self.n1 * self.n2

    def subtract(selt):
        return self.n1 - self.n2

    def divide(self):
        return self.n1 / self.n2

simple_calc = SimpleCalc(number1, number2)
action = getattr(simple_calc, action)
result = action()
print result


# In[ ]:

import os
os.listdir('/tmp')


# https://docs.python.org/2/library/os.path.html

# In[ ]:

import os

file = '/etc/passwd'

print os.path.isfile(file)
print os.path.isdir(file)
print os.path.exists(file)
print os.path.dirname(file)

print "/tmp" + "/dir1" + "/dir2" + '/file'
print os.path.join('/tmp', 'dir1', 'dir2', 'file')


# In[ ]:

import os
for root, dirs, files in os.walk('/tmp/test1'):
    print root, dirs, files


# In[ ]:

import os
for root, dirs, files in os.walk('/etc'):
    for file in files:
        print os.path.join(root, file)


# In[ ]:

import os
list_of_file_names = []
for root, dirs, files in os.walk('/etc'):
    for file in files:
        list_of_file_names.append(file)

print list_of_file_names


# ### Exercise:
# 
# Using previous example, please create python dictionary 
# that will contain information about file name and its size.
# You can use /etc/ directory.
# 
# Hint 1: remember to check if file exists
# Hint 2: use file name as dictionary key
# 
# 
# Your output should be similar to 'Output example':
# Output example:
# ```python
# {
#     '/etc/sane.d/stv680.conf': 178,
#     '/etc/redhat-release': 33,
#     '/etc/pam.d/cups': 146,
#     '/etc/X11/xinit/Xclients': 2317
#     ...
# }
# ```

# In[ ]:

# SOLUTION

import os
list_of_files = []
for root, dirs, files in os.walk('/etc'):
    for file in files:
        path_to_file = os.path.join(root, file)
        if os.path.isfile(path_to_file):
            list_of_files.append((path_to_file, os.path.getsize(path_to_file)))

files_size = dict(list_of_files)
print files_size


# #### How to sort dictionaries

# In[ ]:

d = {'key1': 1, 'key2': 2, 'key3': 3}

for key in sorted(d, key=d.get):
    print key, d[key]


# ### Exercise:
# 
# Sort dictionary from previous exercise by file size. 
# Largest files should go first.
# 
# Hint: Boot sort and sorted method accept a reverse parameter with a boolean value. 
# This is using to flag descending sorts.

# In[ ]:

# SOLUTION

for key in sorted(files_size, key=files_size.get, reverse=True):
    print key, files_size[key]


# ### Exercise:
# 
# Create a function: get_files_size that will take two arguments: 
# 
# 1. `directory` - string, directory name, e.g.: /etc, by default use '/tmp' directory
# 2. `reverse`   - boolean, if True use descending sorts, by default should be set as False
# 
# Function should return python dictionary that will contain information about file name and its size.
# 
# Please use solutions from previous exercises.
# 
# Example: how to invoke this function?
# 
# ```python
# get_files_size('/etc/', reverse=True) 
# ```
# 
# Additionally: try to execute this function as follows:
# - ```print get_files_size()```
# - ```print get_files_size('/etc')```
# - ```print get_files_size('/etc', reverse=True)```
# 
# 
# Hit: use OrderedDict
# ```python
# from collections import OrderedDict
# ```
# 
# Hint: use itemgetter or lambda notation to get second element from tuple

# In[ ]:

list_of_tuples = [('file1', 100), ('testfile', 2), ('testfile', 3000), ('password', 450)]

list_of_tuples.sort(reverse=True)
print list_of_tuples

# first approach
from operator import itemgetter

list_of_tuples.sort(reverse=True, key=itemgetter(1))
print list_of_tuples


# second approach
list_of_tuples.sort(reverse=True, key=lambda item: item[1])
print list_of_tuples


# #### Lamda expression
# 
# - Lambdas are a shorthand to create anonymous functions in Python (functions without names)
# - are used when for example you want to pass function as argument
# 
# For example you can create function in the 'normal way' using `def` keyword:
# ```python
# def square_root(x): 
#     return math.sqrt(x)
#     
# square_root(2)    
# ```
# or you can use lambda:
# 
# ```python
# square_root = lambda x: math.sqrt(x)
# square_root(2)
# ```
# 
# Another example:
# 
# ```python
# def name(arguments):
#     return expression
# ```
# can be translated to
# ```python
# name = lambda arguments: expression
# ```
# 
# Source:
# - https://docs.python.org/2/reference/expressions.html
# - https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/

# In[ ]:

# SOLUTION

import os
from collections import OrderedDict
from operator import itemgetter

def get_files_size(directory='/tmp', reverse=False):
    list_of_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            path_to_file = os.path.join(root, file)
            if os.path.isfile(path_to_file):
                list_of_files.append((path_to_file, os.path.getsize(path_to_file)))
    
    return OrderedDict(sorted(list_of_files, key=itemgetter(1), reverse=reverse))
            

print get_files_size('/etc')


# In[ ]:

print get_files_size()


# #### User input
# 
# You can choose one of the following methods:
# 
# 1. Function ```input``` or ```raw_input```
# 2. Attribute (dictionary) ```argv``` from module ```sys```
# 3. Dedicated user-friendly command line interface like ```argparse```
#     - https://docs.python.org/3/library/argparse.html
# 
# 

# In[ ]:

your_input = raw_input('Please provide file name: ')
print your_input


# In[ ]:

# python your_script.py argument1 argument2

import sys

script_name = sys.argv[0] # script name, e.g.: your_script
arg1 = sys.argv[1] # first argument, e.g.: argument1
arg2 = sys.argv[2] # second argument, e.g.: argument2


# In[ ]:

import argparse

parser = argparse.ArgumentParser(description='Script to list out files from given directory')

parser.add_argument('--directory', '-d', required=True, help='Source directory')
parser.add_argument('--verbose', '-v', action='store_true', help='If set, print more details')

args = parser.parse_args()

print "directory: ", args.directory
print "verbose:   ", args.verbose


# #### Python file as standalone program
# 
# https://docs.python.org/3/library/__main__.html
# 
# - `'__main__'` is the name of the scope in which top-level code executes
# - A module’s `__name__` is set equal to `'__main__'` when read from standard input, a script, or from an interactive prompt.
# 
# 
# ```python
# def func1():
#     print "func1"
#     
# def func2():
#     print "func2"
# 
# if __name__ == '__main__':
#     # execute only if run as a script
#     # good place to use argparse module to catch user input
#     func1()
#     func2()
#     
# ```

# ### Exercise:
# 
# Using previous exercises create a script that will ask user to provide directory name and sorting order.
# and list out each file from provided directory and its size.
# 
# You can use function get_files_size.
# 
# Input arguments:
# 1. `directory` - string, directory name, e.g.: /etc, by default use '/tmp' directory
# 2. `reverse`   - boolean, if True use descending sorts, by default should be set as False
# 

# In[ ]:

# SOLUTION

# How to run this script:
# python get_files_size.py  --directory /etc 
# python get_files_size.py  --directory /etc --reverse

import os
from collections import OrderedDict
from operator import itemgetter

def get_files_size(directory='/tmp', reverse=False):
    list_of_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            path_to_file = os.path.join(root, file)
            if os.path.isfile(path_to_file):
                list_of_files.append((path_to_file, os.path.getsize(path_to_file)))
    
    return OrderedDict(sorted(list_of_files, key=itemgetter(1), reverse=reverse))
            

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Script to list out files from given directory')

    parser.add_argument('--directory', '-d', required=True, help='Source directory')
    parser.add_argument('--reverse', '-v', action='store_true', help='If set, use descending order')

    args = parser.parse_args()    
    
    print get_files_size(directory=args.directory, reverse=args.reverse)


# ### Exercise
# 
# Modify previously created script to write output (list of files and theirs sizes) to file.
# 
# Allow user to provide path to file. Remember that you should have access to this file.
# 
# By default (if no file path specified) write output to /tmp directory and name file as follows:
# `<TIMESTAMP>`_files.out
# 
# where `<TIMESTAMP>` is the current unix timestamp (seconds since Jan 01 1970. (UTC))
# 
# Hint:
# To get unix timestamp:
# ```python
# import time
# timestamp = int(time.time())
# ```
# 
# 
# Input arguments:
# 1. `directory` - string, directory name, e.g.: /etc, by default use '/tmp' directory
# 2. `reverse`   - boolean, if True use descending sorts, by default should be set as False
# 3. `file_path` - string, specifies the path of output file on disk

# In[ ]:

# SOLUTION

# How to run this script:
# python get_files_size.py  --directory /etc 
# python get_files_size.py  --directory /etc --reverse
# python get_files_size.py  --directory /etc --file_path /tmp/output

import sys
import os
import time
from collections import OrderedDict
from operator import itemgetter

def get_files_size(directory='/tmp', reverse=False):
    list_of_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            path_to_file = os.path.join(root, file)
            if os.path.isfile(path_to_file):
                list_of_files.append((path_to_file, os.path.getsize(path_to_file)))

    return OrderedDict(sorted(list_of_files, key=itemgetter(1), reverse=reverse))

def get_timestamp():
    return int(time.time())

def write_to_file(file_path, dict_to_write):
    if not file_path:
        file_path = os.path.join('/tmp', "{}_files.out".format(get_timestamp()))

    try:
        with open(file_path, 'w') as f:
            for key, value in dict_to_write.items():
                f.write("{} {}\n".format(key, value))
    except IOError as exc:
        print "Cannot write output to file, ", exc
        sys.exit(1)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Script to list out files from given directory')

    parser.add_argument('--directory', '-d', required=True, help='Source directory')
    parser.add_argument('--reverse', '-v', action='store_true', help='If set, use descending order')
    parser.add_argument('--file_path', '-o', help='Output file path')

    args = parser.parse_args()

    files_size_dict = get_files_size(directory=args.directory, reverse=args.reverse)

    write_to_file(file_path=args.file_path, dict_to_write=files_size_dict)


# #### How to execute external commands in python
# 
# To execute external command commands (shell commands) you can choose one of the following methods:
# 1. `os.system("command")`
# 2. `stream = os.popen("command")`
# 3. `subprocess.call("command")` - recommended, it replaces above-mentioned commands
# 
# Sources:
# - https://docs.python.org/2/library/subprocess.html#module-subprocess
# - https://docs.python.org/2/library/subprocess.html#subprocess-replacements
# - https://pymotw.com/2/subprocess/

# In[ ]:

import subprocess
print subprocess.call("uname -a", shell=True) # returns only exit code


# In[ ]:

import subprocess
print subprocess.check_output("uname -a", shell=True)


# In[ ]:

# list out all account names with /sbin/nologin shell (politely refuse a login) from /etc/passwd file
# equivalent to: 
# cat /etc/passwd | grep /bin/false | cut -f 1 -d:

import subprocess

cat = subprocess.Popen(['cat', '/etc/passwd'], 
                        stdout=subprocess.PIPE)

grep = subprocess.Popen(['grep', '/sbin/nologin'],
                        stdin=cat.stdout,
                        stdout=subprocess.PIPE)

cut = subprocess.Popen(['cut', '-f', '1', '-d:'],
                        stdin=grep.stdout,
                        stdout=subprocess.PIPE)

nologin_accounts = cut.stdout
print nologin_accounts

nologin_accounts = [account.strip() for account in nologin_accounts]
print nologin_accounts


# ### Exercise
# 
# Create a script that will execute "ps -aux" command. Collect first 10 lines only.

# In[ ]:

# SOLUTION

import subprocess

output = subprocess.check_output("ps -aux", shell=True)
output_list = output.split('\n')

for index, line in enumerate(output_list[:10]):
    print "{}) {} \n".format(index, line)


# In[ ]:

# ALTERNATIVE SOLUTION

import subprocess

ps_aux = subprocess.Popen(['ps', '-aux'], 
                        stdout=subprocess.PIPE)

head = subprocess.Popen(['head', '-n10'],
                        stdin=ps_aux.stdout,
                        stdout=subprocess.PIPE)

processes = head.stdout
for index, line in enumerate(processes):
    print "{}) {} \n".format(index, line)


# #### Data persistence

# In[ ]:

import json

data = {'int': 100, 'string': 'string', 'bool': True,  'list': [1, 2, 3, 4], 'dict': {'key1': 1, 'key2': 2}}

print json.dumps(data, indent=4)


# #### HTTP for Humans
# 
# http://docs.python-requests.org/en/master/

# In[ ]:

import requests

r = requests.get('http://date.jsontest.com/')

print r.text

print r.json()


# In[ ]:

import requests

r = requests.get('http://date.jsontest.com/')

data = r.json()
print "Date: ", data['date']
print "Timestamp: ", data['milliseconds_since_epoch']
print "Time: ", data['time']


# In[36]:

import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)

print r.url
print r.json()


# In[ ]:

import os
import requests
from BeautifulSoup import BeautifulSoup

url = "https://www.python.org/ftp/python/"
r = requests.get(url)

soup = BeautifulSoup(r.text)
links = soup.findAll('a', href=True)

for link in links:
    python_version = link['href']
    
    r = requests.get(os.path.join(url, python_version))
    
    soup = BeautifulSoup(r.text)
    links = soup.findAll('a', href=True)
    
    for link in links:
        if link['href'].endswith('exe'):
            print os.path.join(url, link['href'])


# ### Exercise
# 
# List out all url to '.exe' files from this site https://www.python.org/ftp/python/3.5.1/
# 
# Hint:
# - pip install requests
# - pip install BeautifulSoup
# - https://www.crummy.com/software/BeautifulSoup/bs3/documentation.html

# In[ ]:

import os
import requests
from BeautifulSoup import BeautifulSoup

url = "https://www.python.org/ftp/python/3.5.1/"
r = requests.get(url)

soup = BeautifulSoup(r.text)
links = soup.findAll('a', href=True)

for link in links:
    if link['href'].endswith('exe'):
        print os.path.join(url, link['href'])


# In[ ]:




# In[ ]:



