
# coding: utf-8

# # Applied Python (Python in practice)

# #### The Python Standard Library
# 
# https://docs.python.org/2/library/

# In[2]:

import datetime
#from datetime import date

print(datetime.date.today())

day_today = datetime.date.today().strftime("%A")
print("Today is {day}".format(day=day_today))
print("Today is {}".format(day_today))


# In[3]:

# IF/ELSE 

print("Monday" == "Friday")

bool_value = True
print("here", bool_value is not False)

if day_today == "Friday":
    print("Today is Friday!!")
else:
    print("Today is {day}".format(day=day_today))
    
l = [1,2,3] 
if len(l) > 0: # NOT PYTHONIC WAY
    print("-------> ok")

print(bool(l))
print(bool({}))
if l:          # PYTHONIC WAY
    print("ok")


# In[15]:

# IN operator

month_today = datetime.date.today().strftime("%B")
print(month_today)

month_today = "May"

day_today = "Saturday"
# not Pythonic
if day_today == "Saturday" or day_today == "Sunday":
    if month_today == "June":
        print("Today is {day}! Hurray! The weekend has landed!".format(day=day_today))
else:
    print("Nope. It isn't weeked. Today is {day}".format(day=day_today))
    
# Pythonic
if day_today in ['Saturday', 'Sunday']:
    print("Today is {day}! Hurray! The weekend has landed!".format(day=day_today))
else:
    print("Nope. It isn't weeked. Today is {day}".format(day=day_today))


# In[23]:

# FOOR LOOP

# multiply each number by 2

numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    print(number * 2)
    
print([(number, number * 2) for number in numbers])

L_TEMP = []
for number in numbers:
    if number % 2 == 0:
        L_TEMP.append(number * number)
print(L_TEMP)

# LIST COMPREHENSION (with filter)
L_TEMP = [number * number for number in numbers if number % 2 == 0] # VERY PYTHONIC
print(L_TEMP)


# In[ ]:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# numbers = range(1, 11)

for number in numbers:
    if number % 2 == 0:
        print("Number {} is even".format(number))
    elif number % 2 == 1:
        print("Number {} is odd".format(number))
    else:
        print("is it number: {}?".format(number))


# In[ ]:

# List comprehension - Pythonic way of doing stmh

# modulo (%) operation finds the remainder after division of one number by another

# Even numbers always end with a digit of 0, 2, 4, 6 or 8
even_numbers = [number for number in range(1,11) if number % 2 == 0]
print("Even numbers: ", even_numbers)

# Odd numbers always end with a digit of 1, 3, 5, 7, or 9
odd_numbers = [number for number in range(1,11) if number % 2 == 1]
print("Odd numbers:", odd_numbers)


# In[25]:

# SETS

s = set([1, 2, 3, 2 ,4, 5, 5])
print("s: ", s)

numbers = range(1, 11)
even_numbers = [number for number in range(1,11) if number % 2 == 0]

even_numbers = set(even_numbers)
print(even_numbers)
numbers = set(numbers)
print(numbers)

# difference (-) -> new set with elements in numbers but not in even_numbers
# so we can get odd_numbers

odd_numbers = list(numbers - even_numbers)
print("Odd numbers: ", odd_numbers)


# In[ ]:

# WHILE LOOP, BREAK

while True:
    number = input("Please provide number: ")
    if number % 2 == 0:
        print("Number {} is even".format(number))
    elif number % 2 == 1:
        print("Number {} is odd".format(number))
    else:
        print("is it number: {}?".format(number))
    break


# In[ ]:

# DEF, RETURN

def is_number_even(number):
    if number % 2 == 0:
        print("Number {} is even".format(number))
        return True
    elif number % 2 == 1:
        print("Number {} is odd".format(number))
    else:
        print("is it number: {}?".format(number))
    return False


while True:
    number = input("Please provide number: ")
    is_number_even(number)
    break


# In[ ]:

# TRY/EXCEPT

def fn():
    number = input("Please provide number: ")
    try:
        number = int(number)
        print(number)
    except ValueError as exc:
        print("Do we have number or not?)
    
    try:
        is_number_even(number)
    except Exception as exc:
        print(exc)
    
fn()


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

print("You will {action} two numbers {number1} and {number2}".format(**locals()))

result = actions[action](number1, number2)
#result = actions.get(action)(number1, number2)

print("Result is: ", result)


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


action = raw_input("Choose one action [add|multiply|subtract|divide|]:")
number1 = raw_input("Provide first number: ")
number2 = raw_input("Provide second number: ")

# convert to int
number1 = int(number1)
number2 = int(number2)

simple_calc = SimpleCalc(number1, number2)

action = getattr(simple_calc, action)
result = action()
print(result)


# ## Let's practice

# In[26]:

import os
list_of_dirs = os.listdir('/tmp')

print(list_of_dirs)

for file_or_dir in list_of_dirs:
    if os.path.isfile("/tmp/" + file_or_dir):
        print("File: ", file_or_dir)
    elif os.path.isdir("/tmp/" + file_or_dir):
        print("Directory: ", file_or_dir)        


# https://docs.python.org/2/library/os.path.html

# In[29]:

import os

file = '/etc/passwd'

print(os.path.isfile(file))
print(os.path.isdir(file))
print(os.path.exists(file))
print(os.path.dirname(file))

print("/tmp" + "/dir1" + "/dir2" + '/file')
print(os.path.join('/tmp', 'dir1', 'dir2', 'file'))

print(os.sep) 


# In[28]:

for root, dirs, files in os.walk('/tmp/'):
    print(root, dirs, files, "\n")


# In[ ]:

import os

root, dirs, files, aaaa = ('root', ['d1', 'd2'], ['f1'], 1)

a, b = 1, 2
print(a, b)

a, b = b, a
print(a, b)


for root, dirs, files in os.walk('/tmp/'):
    print(root, dirs, files)


# In[ ]:

import os
for root, dirs, files in os.walk('/tmp'):
    for file in files:
        print(os.path.join(root, file))


# In[ ]:

import os

list_of_file_names = []
for root, dirs, files in os.walk('/etc'):
    for file in files:
        list_of_file_names.append(os.path.join(root, file))

print(list_of_file_names)


# In[1]:

d = {'key1': 1, 'key2':2}
print(d.items())

e = dict(d.items())
print(e)


# ### Exercise:
# 
# Using previous example, please create python dictionary 
# that will contain information about file name and its size.
# You can use /etc as source directory.
# 
# - Hint 1: remember to check if file exists, `os.path.isfile(path_to_file)`
# - Hint 2: use file path as dictionary key, ` files_size[file_path] = file_size`
# - Hint 3: to create dictionary you can use list of tuples e.g: `dict( [ (key1, value), (key2, value), ...] )`
# - Hint 4: to create path to file, you can concatenate dir path and file name, `os.path.join( directory, file_name )`
# - Hint 5: to get file size: `os.path.getsize(path)`
# 
# 
# Your output should be similar to:
# ```python
# {
#     '/etc/sane.d/stv680.conf': 178,
#     '/etc/redhat-release': 33,
#     '/etc/pam.d/cups': 146,
#     '/etc/X11/xinit/Xclients': 2317
#     ...
# }
# ```

# In[31]:

# SOLUTION

import os
list_of_files = []
for root, dirs, files in os.walk('/etc'):
    for file in files:
        path_to_file = os.path.join(root, file) # root + "/" + file
        if os.path.isfile(path_to_file):
            list_of_files.append((path_to_file, os.path.getsize(path_to_file)))

files_size = dict(list_of_files)
print(files_size)


# In[ ]:

# SECOND SOLUTION

import os
files_size = {}
for root, dirs, files in os.walk('/etc'):
    for file in files:
        path_to_file = os.path.join(root, file)
        try:
            files_size[path_to_file] = os.path.getsize(path_to_file)
        except IOError as exc:
            print(exc)
        except OSError as exc:
            print(exc)
            
print(files_size)


# #### How to sort data structures

# In[36]:

item = None

n = [1, 3, 2, 5, 0]
print(n.sort(), n)

n = [1, 3, 2, 5, 0]
n_sorted = sorted(n)
print(n_sorted, n)


# In[34]:

L = [3, 1, 2]
output = L.sort()
print(output)
print(L)
for item in output:
    print(item)


# In[37]:

list_of_tuples = [('file1', 100), ('testfile', 2), ('testfile', 3000), ('password', 450)]
dict(list_of_tuples)


# In[39]:

# EXAMPLES

list_of_tuples = [('a', 100), ('b', 2), ('c', 3000), ('d', 450)]

list_of_tuples.sort(reverse=False)
print(list_of_tuples)

# first approach
from operator import itemgetter

list_of_tuples.sort(reverse=True, key=itemgetter(1))
print(list_of_tuples)

print(itemgetter(1)('ABCDEFG'))
print(itemgetter(0)([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(itemgetter(0, 2, 4)([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# second approach

list_of_tuples.sort(reverse=True, key=lambda item: item[1])
print(list_of_tuples)


# In[ ]:

# To clarify conversion between dict and list of tuples

d = {'key2': 2, 'key1': 1, 'key3': 3}  # Dictionary


# How to convert dictionary to list of tuples

list_of_tuples = d.items()  # List of tuples: [ (k1, v), (k2, v), (k3, v), ... (kn, v)]
print(list_of_tuples)

# How to convert list of tuples to dictionary

d = dict(list_of_tuples)
print(d)


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

# In[44]:

d = {'key2': 2, 'key1': 1, 'key3': 3}
print(d)

print(sorted(d))
for key in d:
    print(d[key])

print(sorted(d, key=d.get))

for key in sorted(d, key=d.get, reverse=True):
    print(key, d[key])


# ### Exercise:
# 
# Sort dictionary from previous exercise by file size. 
# Largest files should go first.
# 
# - Hint 1: Booth sort and sorted method accept a reverse parameter with a boolean value. 
# This is using to flag descending sorts.
# 
# `d.sort(reverse=True)`

# In[ ]:

# SOLUTION

for key in sorted(files_size, key=files_size.get, reverse=True):
    print(key, files_size[key])
    b
# SOLUTION 2
print(sorted(files_size, key=files_size.get, reverse=True))


# In[ ]:

#import collections
#collections.OrderedDict

from collections import OrderedDict

d = {'key2': 2, 'key1': 1, 'key3': 3}

od = OrderedDict(d.items())

# second way to create sorted dict by value not ket

print(sorted(d.items(), key=d.get, reverse=True))

print(OrderedDict(sorted(d.items(), key=d.get, reverse=True)))


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
# - ```print(get_files_size())```
# - ```print(get_files_size('/etc'))```
# - ```print(get_files_size('/etc', reverse=True))```
# 
# 
# Hit 1: use OrderedDict
# ```python
# from collections import OrderedDict
# ```
# 
# Hint 2: use itemgetter or lambda notation to get second element from tuple

# In[ ]:

# SOLUTION

import os
from collections import OrderedDict
from operator import itemgetter

def get_files_size(directory='/tmp', reverse=False):
    dir(os)
    list_of_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            path_to_file = os.path.join(root, file)
            if os.path.isfile(path_to_file):
                list_of_files.append((path_to_file, os.path.getsize(path_to_file)))
    
    return OrderedDict(sorted(list_of_files, key=itemgetter(1), reverse=reverse))
          
print(get_files_size('/etc'))


# In[ ]:

# SECOND SOLUTION

import os
from collections import OrderedDict
from operator import itemgetter

def get_files_size(directory='/tmp', reverse=False):
    files_size = {}
    for root, dirs, files in os.walk('/etc'):
        for file in files:
            path_to_file = os.path.join(root, file)
            if os.path.isfile(path_to_file):
                files_size[path_to_file] = os.path.getsize(path_to_file)
    
    return OrderedDict(sorted(files_size.items(), key=itemgetter(1), reverse=reverse))
            
print(get_files_size('/etc'))


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

# In[45]:

your_input = raw_input('Please provide file name: ')
print(your_input)


# In[ ]:

# python your_script.py argument1 argument2

import sys

# $0 - script name, $1 .. $9 - args
script_name = sys.argv[0] # script name, e.g.: your_script
arg1 = sys.argv[1] # first argument, e.g.: argument1
arg2 = sys.argv[2] # second argument, e.g.: argument2


# In[ ]:

import argparse # since 2.7, or optparse, click (py3)

# python script.py --directory /etc
# python script.py -d /etc
# python script.py -d /etc --verbose


parser = argparse.ArgumentParser(description='Script to list out files from given directory')

parser.add_argument('--directory', '-d', required=True, help='Source directory')
parser.add_argument('--verbose', '-v', action='store_true', help='If set, print more details')

args = parser.parse_args()

print("directory: ", args.directory)
print("verbose:   ", args.verbose)


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
#     print("func1")
#     
# def func2():
#     print("func2")
# 
# if __name__ == '__main__':
#     # execute only if run as a script
#     # good place to use argparse module to catch user input
#     func1()
#     func2()
#     
# ```

# In[ ]:

def do_something(directory, verbose):
    print("directory: ", directory)
    print("verbose:   ", verbose)
    

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='Script to list out files from given directory')

    parser.add_argument('--directory', '-d', required=True, help='Source directory')
    parser.add_argument('--verbose', '-v', action='store_true', help='If set, print more details')

    args = parser.parse_args()

    do_something(directory=args.directory, verbose=args.verbose)


# ### Exercise:
# 
# Using previous exercises create a script that will ask user to provide directory name and sorting order.
# List out each file from provided directory and its size.
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
    files_size = {}
    for root, dirs, files in os.walk('/etc'):
        for file in files:
            path_to_file = os.path.join(root, file)
            if os.path.isfile(path_to_file):
                files_size[path_to_file] = os.path.getsize(path_to_file)
    
    return OrderedDict(sorted(files_size.items(), key=itemgetter(1), reverse=reverse))
            

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Script to list out files from given directory')

    parser.add_argument('--directory', '-d', required=True, help='Source directory')
    parser.add_argument('--reverse', '-r', action='store_true', help='If set, use descending order')

    args = parser.parse_args()    
    
    print(get_files_size(directory=args.directory, reverse=args.reverse))


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
# Hint 1:
# To get unix timestamp:
# ```python
# import time
# timestamp = int(time.time())
# ```
# 
# Hint 2: You can write your own function to write output to file
# 
# Input arguments:
# 1. `directory` - string, directory name, e.g.: /etc, by default use '/tmp' directory
# 2. `reverse`   - boolean, if True use descending sorts, by default should be set as False
# 3. `file_path` - string, specifies the path of output file on disk

# In[ ]:

# How to write to file

f = open('/tmp/file', 'w')

f.write('first line\n')
f.write('second line\n')
f.write('third line\n')

f.close()


# In[ ]:

# How to write to file

with open('/tmp/file', 'w') as f:

    f.write('first line\n')
    f.write('second line\n')
    f.write('third line\n')


# In[ ]:

list_of_lines = ['line1', 'line2', 'line3']

with open('/tmp/file', 'w') as f:
    for line in lines:
        f.write("{} \n".format(line))

# or even better

list_of_lines = ["{} \n".format(line) for line in list_of_lines]
with open('/tmp/file', 'w') as f:
    f.writelines(list_of_lines)


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
    files_size = {}
    for root, dirs, files in os.walk('/etc'):
        for file in files:
            path_to_file = os.path.join(root, file)
            if os.path.isfile(path_to_file):
                files_size[path_to_file] = os.path.getsize(path_to_file)
    
    return OrderedDict(sorted(files_size.items(), key=itemgetter(1), reverse=reverse))

def get_timestamp():
    return int(time.time())

def write_to_file(file_path, dict_to_write):
    if not file_path:
        file_path = os.path.join(os.sep, 'tmp', "{}_files.out".format(get_timestamp()))

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
# To execute external commands (shell commands) you can choose one of the following methods:
# 1. `os.system("command")`
# 2. `stream = os.popen("command")`
# 3. `subprocess.call("command")` - recommended, it replaces above-mentioned commands
# 
# Sources:
# - https://docs.python.org/2/library/subprocess.html#module-subprocess
# - https://docs.python.org/2/library/subprocess.html#subprocess-replacements
# - https://pymotw.com/2/subprocess/

# In[48]:

import subprocess
print(subprocess.call("uname -a", shell=True)) # returns only exit code


# In[ ]:

import subprocess
output = subprocess.check_output("cat /etc/passwd | grep /sbin/nologin | cut -f 1 -d:", shell=True)
for item in output.split(" "):
    print(item)


# In[ ]:

# list out all account names with /sbin/nologin shell (politely refuse a login) 
# from /etc/passwd file
# equivalent to: 
# cat /etc/passwd | grep /sbin/nologin | cut -f 1 -d:

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
print(nologin_accounts)

nologin_accounts = [account.strip() for account in nologin_accounts]
print(nologin_accounts)


# ### Exercise
# 
# Create a script that will execute "ps -aux" command. Collect first 10 lines only.

# In[65]:

s = "item\n item2\n item3"
s.split("\n")


# In[61]:

# SOLUTION

import subprocess

output = subprocess.check_output("ps -aux", shell=True)
output_list = output.split('\n')

for index, line in enumerate(output_list[:10]):
    print("{}) {}".format(index, line))


# In[60]:

# ALTERNATIVE SOLUTION

import subprocess

ps_aux = subprocess.Popen(['ps', '-aux'], 
                        stdout=subprocess.PIPE)

head = subprocess.Popen(['head', '-n10'],
                        stdin=ps_aux.stdout,
                        stdout=subprocess.PIPE)

processes = head.stdout
for index, line in enumerate(processes):
    print("{}) {} \n".format(index, line))


# #### Data persistence

# In[72]:

import json
# import simplejson

data = {'int': 100, 'string': 'string', 'bool': True,  'list': [1, 2, 3, 4], 'dict': {'key1': 1, 'key2': 2}}
print(type(data), data)

data_json = json.dumps(data, indent=4)
print(type(data_json), data_json)

data2 = json.loads(data_json)
print(data2)

print(json.dumps({"msg": "error"}))


# #### HTTP for Humans
# 
# http://docs.python-requests.org/en/master/

# In[73]:

import requests

r = requests.get('http://date.jsontest.com/')

print(r.text)
print(r.json())


# In[74]:

import requests

r = requests.get('http://date.jsontest.com/')

data = r.json()
print("Date: ", data['date'])
print("Timestamp: ", data['milliseconds_since_epoch'])
print("Time: ", data['time'])


# In[ ]:

import os
import requests
from BeautifulSoup import BeautifulSoup

url = "https://www.python.org/ftp/python/"
r = requests.get(url)

print(r.text)


# In[75]:

import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)

print(r.url)
print(r.json())


# In[80]:

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
            print(os.path.join(url, python_version, link['href']))


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
        print(os.path.join(url, link['href']))


# #### The ElementTree XML API
# 
# https://docs.python.org/2/library/xml.etree.elementtree.html

# In[82]:

country_data = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
"""


# In[83]:

import xml.etree.ElementTree as ET

# if you want to read XML data from file
#tree = ET.parse('country_data.xml')
#root = tree.getroot()

root = ET.fromstring(country_data)

countries = root.findall('country')
for country in countries:
    print("Country: ", country.get('name'))
    
    country_neighbours = country.findall('neighbor')
    for neighbor in country_neighbours:
        print("Neigbor: ", neighbor.get('name'))
        
    print("-" * 30)


# In[ ]:

python -m SimpleHTTPServer


# ### Databases
# 
# https://docs.python.org/2/library/sqlite3.html
# http://docs.sqlalchemy.org/en/latest/dialects/sqlite.html
# 

# #### SQLite

# In[6]:

import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
c.execute("INSERT INTO stocks VALUES ('2006-02-05','BUY','RHAT2',101,40.24)")

# Save (commit) the changes
conn.commit()
conn.close()


# In[7]:

import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)


# #### SQLAlchemy

# In[19]:

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'
  
  id = Column(Integer, primary_key=True)
  name = Column(String)
  fullname = Column(String)
  password = Column(String)
  
  def __init__(self, name, fullname, password):
      self.name = name
      self.fullname = fullname
      self.password = password

  def __repr__(self):
     return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)
    
    
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

user1 = User('Vincent', 'Vega', 'aaaa1')
user2 = User('Butch', 'Coolidge', 'watch22')

print(user1, user2)

Session = sessionmaker(bind=engine)
session = Session()

session.add_all([user1, user2])
session.commit()


print("-->", session.query(User).filter_by(name='Vincent').first())


# In[ ]:



