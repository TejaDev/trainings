
# coding: utf-8

# # Python Training - Basic Level

# ### Overview
# 
# ##### What is Python:
# 
# - an interpreted (byte code compilation) object-oriented programming language
# - dynamic typing (run time type checking), very high level dynamic data types and classes
# - strong typing (variables are bound to a particular data type)
# - very clear syntax - Python Style Guide: https://www.python.org/dev/peps/pep-0008/ 
# - portable: it runs on many Unix variants, on the Mac, and on PCs under MS-DOS, Windows, Windows NT, and OS/2
# - easily extensible with C/C++/Java code, and easily embeddable in applications
# - free to use, even for commercial products, because of open source license
# 
# > 
# The joy of coding Python should be in seeing short, concise, readable classes that express a lot of action in a small amount of clear code -- not in reams of trivial code that bores the reader to death - Guido van Rossum
# 
# 
# 
# Sources:
# - https://docs.python.org/2/faq/general.html
# - https://www.python.org/download/releases/2.7/license/
# - http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html - programming lanugages trends
# - https://github.com/blog/2047-language-trends-on-github - gitub trends
# - https://www.python.org/doc/essays/comparisons/ - comparing python to other languages

# ### What is Python good for
# 
# - text processing & web scraping (reqgular expressions, LXML, Beautiful Soup, ...)
# - integration with operating systems (system calls, filesystems, TCP/IP sockets)
# - supprort for all known internet protocols (HTTP, FTP, SMTP, XML-RPC, POP, SOAP, ...)
# - data science (NumPy, SciPy, and matplotlib)
# - writing Web Applications (Django, Flask, Pyramid, ...)
# - glue together large software components
# - GUI programming (Tk, Qt, GNOME, KDE, Kivy ...)
# 
# Sources:
# - https://wiki.python.org/moin/WebFrameworks
# - https://www.python.org/doc/essays/omg-darpa-mcc-position/ - Glue It All Together With Python
# - http://scikit-learn.org/stable/
# - https://wiki.python.org/moin/GuiProgramming

# ### Python strenghts - comparing to other languages
# 
# - Easy to learn
# - Application prototyping 
#     - Program development using Python is 5-10 times faster than using C/C++ and 3-5 times faster than using Java
#     - In many cases, a prototype of an application can be written in Python without writing any C/C++/Java code
# - Supports multiple programming paradigms
#     - procedural (statement based)
#     - object-oriented (polymorphism, operator overloading and multiple inheritance)
#     - functional (generators, comprehensions, closures, maps, decorators, lambdas, first-class function objects)
# - Portability
# - Automatic memory management
#     - objects are automatically allocated and reclaimed (“garbage collects”) 
# - Third-party utilities
#     - more than 70k packages
#     - https://pypi.python.org/pypi
#     
#     
# Sources:
# - https://www.python.org/doc/essays/omg-darpa-mcc-position/

# #### Software that makes use of Python
# 
# - Applications: Dropbox, Youtube, Instagram, Reddit, Spotify, Blender 3D, ...
# - Games: Civilization IV, Eve Online
# - Tools: Ansible, Mercurial 
# 
# Sources:
# - https://www.python.org/about/success/
# - https://wiki.python.org/moin/OrganizationsUsingPython
# - https://wiki.python.org/moin/Applications

# ### History of Python
# 
# 
# - Python was created in the early 1990s by Guido van Rossum at the National Research Institute for Mathematics and Computer Science in the Netherlands
# 
# - Python is derived from many other languages, including ABC, Modula-3, C, C++, Algol-68, SmallTalk, and Unix shell and other scripting languages.
# 
# - The language was named after the BBC show “Monty Python’s Flying Circus”
# 
# - Python 2.7.y from 2010 - most common used Python version but legacy
# - Python 3.x.y from 2008 - recommended version
# 
# 
# Sources:
# - http://python-history.blogspot.com/
# - https://docs.python.org/2.7/faq/design.html 
# - https://www.python.org/download/releases/2.7/license/
# - https://www.python.org/downloads/ - here you can find all Python version and release dates
# - https://www.python.org/~guido/interviews.html - interviews with python creator

# ### Python 2.x or Python 3.x
# 
# - Official statement: **Python 2.x is legacy, Python 3.x is the present and future of the language**
# - But in practice:
#     -  Python 2.7.x has been standard for a long time
#     -  Python 2.7.x will receive necessary security updates until 2020
# 
# Major differences:
# - print is a function not statement
# - Better Unicode support
# - Memory-efficient iterable returns by default
# - Integers can handle any size, no longer limited to the machine's word size
# 
# 
# Sources:
# - https://wiki.python.org/moin/Python2orPython3
# - http://docs.python-guide.org/en/latest/starting/which-python/#the-state-of-python-2-vs-3
# - https://docs.python.org/3/whatsnew/3.0.html - What is new in Python 3.x
# - http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html - Python 3 Q&A
# - http://getpython3.com/ - How to port from 2.x to 3.x
# - https://python3wos.appspot.com/ - List of packages supported in Python 3.x, Most useful and not yet supported (January 2016): Fabric, Ansible, suds, protobuf, M2Crypto

# ### Python implementations
# 
# - Python is actually a specification for a language that can be implemented in many different ways
# - You can find Python Grammar specification here: https://docs.python.org/2/reference/grammar.html
# 
# Python implementations:
# 
# - CPython
#     - reference implementation of Python, written in C
#     - it compiles Python code to intermediate bytecode which is then interpreted by a virtual machine
#     
# - PyPy
#     - interpreter implemented in a restricted statically-typed subset of the Python language
#     - Python performance was improved - it is 5 times faster than CPython
#     
# - Jython
#     - implementation that compiles Python code to Java bytecode which is then executed by the JVM
#     - it is possible to import and use any Java class like a Python module
#     - examples: https://wiki.python.org/jython/LearningJython
#     - http://www.jython.org/jythonbook/en/1.0/SimpleWebApps.html
#     
# - IronPython
#     - implementation of Python for the .NET framework
#     - it is possible to import and use any .NET framework libraries

# ### Interpreter
# 
# - A kind of program that executes other programs
# - Reads your program and carries out the instructions it contains
# 
# 
# http://aosabook.org/en/500L/a-python-interpreter-written-in-python.html

# ### Code compilation and interpreting
# 
# #### Byte code
# 
# - When you execute a script, Python compiles your source code into a format known as byte code
#     - it creates binary file with .pyc extension
#         - in python 3.x, .pyc files are stored in ```__pycache__``` directory
#         - byte code can be also generated in memory in case have no write permission in filesystem
#     - compilation is simply a translation step
# - Byte code is a lower-level, platform-independent representation of your source code
# - Byte code translation is performed to speed execution
# 
# > Byte code is an implementation detail of the CPython interpreter
# 
# - Byte code example:
# 
# ```python
# 0 LOAD_GLOBAL              0 (len)
# 3 LOAD_FAST                0 (alist)
# 6 CALL_FUNCTION            1
# 9 RETURN_VALUE
# ```
# 
# #### Byte code interpretation
# 
# - Byte code instructions are interpreted by python interpreter
#     - interpreter reads the binary file (.pyc) and executes the instructions one at a time
# 
# 
# #### Compilation and interpretation steps
# 
# For example:
# 
# ```python
# python your_program.py
# ```
# 
# 1. Lexical analysis (break text to find tokens - keywords, operators, literals)
# 2. Parsing - based on the rules from grammar, produces Abstract Syntax Tree (AST)
# 3. Code generation produces PyCodeObject (bytecode)
# 4. Code execution by bytecode interpreter (stack-based virtual machine)
# 
# Sources:
# - http://security.coverity.com/blog/2014/Nov/understanding-python-bytecode.html
# - http://tomlee.co/wp-content/uploads/2012/11/108_python-language-internals.pdf

# ### How to install Python
# 
# For Windows, Mac OS X, Sources:
# 
#     - download Python interpreter from https://www.python.org/downloads/
#     - detailed instruction for Windows: http://www.howtogeek.com/197947/how-to-install-python-on-windows/
#     
# For Linux:
#     - just use your package manager like apt, yum
#         - for RedHat like systems: yum install python
#         - for Debian like systems: apt-get install python

# ### Interactive mode
# 
# What is interactive mode and why it should be used:
# - command line shell for Python
# - immediate feedback for each statement you type
# - it is faster to check Python documentation than using Web Browser, just type
# ```python
# help(antyhing)
# ```
# 
# How to run interactive mode:
# 
# - Just invoke the interpreter without passing a script file as a parameter 
# 
# - To enter the interactive mode type **python** command in your Shell (windows/linux)
# - You should be able to see prompt **>>>**
# 
# For example:
# 
# ```python
# Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>>
# ```
# 
# Sources:
# - http://stackoverflow.com/questions/2664785/why-use-python-interactive-mode

# ### Script mode
# 
# - Python program/script is just a text file containing Python statements
# 
# - Invoking the interpreter with a script parameter begins execution of the script and continues until the script is finished
# - Python files have extension .py, for example: hello_world.py
# - How to run? (you should have python interpreter set in PATH environment variable)
# 
# ```bash
# python your_script.py
# ```
# 
# - You can also run your python script as follows:
# 
# ```bash
# ./your_script.py
# ```
# 
# - but you need to add path to your python interpreter directly inside your script
# 
# ```python
# #!/usr/bin/python
# print "Hello world"
# ```

# ### Syntax
# 
# #### Code structure
# 
# - Remember: A Python program is read by a parser
# - A Python program is divided into a number of logical lines
# - The end of a logical line is represented by the token NEWLINE
# - A logical line is constructed from one or more physical lines
# - A physical line is a sequence of characters terminated by an end-of-line sequence
# - Two or more physical lines may be joined into logical lines using backslash characters (\)
# 
# #### Indentation
# 
# - Indentation = white spaces (tabs or spaces - never mixed!)
# - Indentation level of your statements is significant
# - Everywhere else, whitespace is not significant and can be used as you like, just like in any other language
# - The exact amount of indentation doesn't matter at all, but only the relative indentation of nested blocks (relative to each other)
# 
# - Python uses indentation to indicate blocks of code
# - https://www.python.org/dev/peps/pep-0008/
# 
# ```python
# def function(args):
#     do_something()               # Indentation
#     do_something_else()          # Indentation
#     return                       # Indentation
# 
# def function2(condition):
#     if condition == 0:           # Indentation
#         do_something()           # Indentation
#         if condition == 1:       # Indentation
#             do_something_else()  # Indentation
#         else:                    # Indentation
#             print('do nothing')  # Indentation
#     else:                        # Indentation
#         do_something()           # Indentation
#         
#                                  # two empty lines - does not matter 
#      return                      # Indentation
#     
# function()
# function2()
# 
# ```
# 
# 
# #### Keywords (reserved words)
# 
# - Important: all the Python keywords contain lowercase letters only
# - These names below cannot be used as ordinary identifiers:
# 
# ```
# and       del       from      not       while
# as        elif      global    or        with
# assert    else      if        pass      yield
# break     except    import    print
# class     exec      in        raise
# continue  finally   is        return
# def       for       lambda    try
# ```
# 
# 
# #### Operators
# 
# - The following tokens are operators:
# 
# ```
# +       -       *       **      /       //      %      @
# <<      >>      &       |       ^       ~
# <       >       <=      >=      ==      !=
# ```
# 
# #### Comments
# 
# - Represented by a hash sign(#) that is not inside a string literal
# - Represented by quotation - you can use single ('), double (") and triple (''' or """) quotes
# 
# 
# Sources:
# - https://docs.python.org/2/reference/lexical_analysis.html
# - https://docs.python.org/3/reference/lexical_analysis.html

# In[30]:

# comment
# comment

a = 3 #comment

'''
comment
comment
comment
'''


# ### Variables are labels, not boxes
# 
# - So it’s better to think of them as labels (names) attached to objects
# 
# - Always read the right-hand side first: that’s where the object is created or retrieved
# - After that, the variable on the left is bound to the object, like a label stuck to it
# 
# - A variable is simply a value bound to a name
# - The value has a type -- like "integer" or "string" or "list" -- but the label (variable) itself doesn't
# 
# 
# - Created when they are first assigned values (dynamic typing)
# - Replaced with their values when used in expressions
# - Must be assigned before they can be used in expressions
# - Refer to objects and are never declared ahead of time
# 
# #### Labeling object - example
# 
# ```python
# >>> A = 1                # Assign a name to an object
# ```
# 
# 1. Create an object to represent the VALUE 1
# 2. Create the LABEL A, **if it does not yet exist**
# 3. Link the LABEL A to the new object 1
# 

# ### Dynamic & strong typing
# 
# > Once you create an object, you bind its operation set for all time
# — you can perform only string operations on a string and list operations on a list
# 
# - Type checks are performed mostly at run time
# - Interpreter tracks of the kinds of objects your program uses when it runs
# - Dynamic typing means there is less code for you to write
# 
# - Sort of type-dependent behavior is known as polymorphism 
# - Every operation is a polymorphic operation in Python: 
# 
# > Polymorphic behavior has in recent years come to also be known as duck typing—the essential idea being that your code is not supposed to care if an object is a duck, only that it quacks. Anything that quacks will do, duck or not, and the implementation of quacks is up to the object,

# In[2]:

# Dynamic programming traps via Python

important_variable = 10
for i in range(1000):
    important_varaible = important_variable + 10   # TYPO in important_VarAible
    
print(important_variable)


# In[3]:

2 + "a"


# ### Built-in types
# 
# - All build-in types listed in documentation: https://docs.python.org/3/library/stdtypes.html
# - Of course you may create your own types (class)
# 
# 
# #### Boolean 
# - True: 1, all numbers without 0, non empty strings, non empty collections
# - False: [], {}, 0, None, ''
# - you can use bool() function to check if object has True or False value
# 
# #### Numeric
# - int(signed integers), float (floating point real values), complex (complex numbers)
# - Number data types store numeric values
# - Of course it is possible to convert between types: int(), float()
# 
# #### Strings
# - Python’s strings also come with full Unicode support required for processing text in internationalized character sets
# - You can find common string operations in 'string' module: https://docs.python.org/2/library/string.html
# 
# > The string module contains a number of useful constants, methods and classes
# 
# Useful contastants in string module:
# - string.ascii_letters -> 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# - string.digits        -> '0123456789'
# - string.punctuation   -> ```'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'``
# 
# 
# Useful string methods:
# - str.capitalize() -> only first character capitalized and the rest lowercased in string
# - str.encode(encoding="utf-8") -> return an encoded version of the string as a bytes object
# - str.decode()
# - str.format() -> perform a string formatting operation
# - str.split(sep) -> return a list of the words in the string, using sep as the delimiter string
# - str.join()
# 
# #### Data structures 
# - list, tuples, dictionaries
# - You can find high-performance container datatypes in collections module: https://docs.python.org/2/library/collections.html
# 

# In[31]:

print(0, ' -> ', bool(0)) # False
print(1, ' -> ', bool(1)) # True

print('', ' -> ', bool('')) # False
print('not empty', ' -> ', bool('not empty')) # True

print([], ' -> ', bool([])) # False
print([1, 2, 3], ' -> ', bool([1, 2, 3])) # True


# #### String formatting operation
# 
# str.format()
# - Perform a string formatting operation
# - The string on which this method is called can contain literal text or replacement fields delimited by braces {}
# - Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument
# - Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument
# 
# 
# Sources:
# - http://www.diveintopython.net/native_data_types/formatting_strings.html
# - https://pyformat.info/
# - https://mkaz.github.io/2012/10/10/python-string-format/

# In[32]:

'{} {}'.format('one', 'two')


# In[33]:

'{1} {0}'.format('one', 'two')


# In[34]:

print('{:>30}'.format('align right')) 
print('{:30}'.format('align left'))
print('{:^30}'.format('center'))


# In[35]:

print('{:.3f}'.format(3.141592653589793))  # 3 decimal places


# In[36]:

person = {'name': 'Guido', 'surname': 'van Rossum'}
print('{p[name]} {p[surname]}'.format(p=person))

data = [4, 8, 15, 16, 23, 42]
print('{d[0]} {d[2]}'.format(d=data))


# In[37]:

print("The sum of {} + {} is {}".format(1, 2, 3))

a = 1
b = 2
c = a + b

print("The sum of {a} + {b} is {c}".format(a=a, b=b, c=c))


# #### Unicodes
# Python 3:
# - In Python 3.X, the normal str string handles Unicode text (including ASCII, which is just a simple kind of Unicode)
# - a distinct bytes string type represents raw byte values (including media and encoded text)
# - 2.X Unicode literals are supported in 3.3 and later for 2.X compatibility (they are treated the same as normal 3.X str strings)
# 
# ```python
# >>> 'sp\xc4m'                     # 3.X: normal str strings are Unicode text
# 'spÄm'
# >>> b'a\x01c'                     # bytes strings are byte-based data
# b'a\x01c'
# ```
# 
# Python 2:
# - In Python 2.X, the normal str string handles both 8-bit character strings (including ASCII text) and raw byte values
# - a distinct unicode string type represents Unicode text; and 3.X bytes literals are supported in 2.6 and later for 3.X compatibility (they are treated the same as normal 2.X str strings)
# 
# ```python
# >>> print u'sp\xc4m'              # 2.X: Unicode strings are a distinct type
# spÄm
# >>> 'a\x01c'                      # Normal str strings contain byte-based text/data
# 'a\x01c'
# >>> b'a\x01c'                     # The 3.X bytes literal works in 2.6+: just str
# 'a\x01c'
# 
# >>> string = 'SPAM'
# >>> a, b, c, d = string           # Same number on both sides
# >>> a, d
# ('S', 'M')
# ```
# 
# 
# Sources:
# - https://docs.python.org/3/library/stdtypes.html

# ### Boolean operations (AND, OR, NOT)
# 
# OR
# - ```x or y``` if x is false, then y, else y
# - For or tests, Python evaluates the operand objects from left to right and returns the first one that is true
# - Moreover, Python stops at the first true operand it finds. This is usually called short-circuit evaluation, as determining a result short-circuits (terminates) the rest of the expression as soon as the result is known
# 
# ```python
# >>> 2 or 3, 3 or 2      # Return left operand if true
# (2, 3)                  # Else, return right operand (true or false)
# >>> [] or 3
# 3
# >>>[] or {}
# {}
# ```
# 
# AND
# - ```x and y``` if x is false, then x, else y	
# - Python and operations also stop as soon as the result is known; however, in this case Python evaluates the operands from left to right and stops if the left operand is a false object because it determines the result—falseand anything is always false
# 
# Example 1:
# ```python
# >>> 2 and 3, 3 and 2    # Return left operand if false
# (3, 2)                  # Else, return right operand (true or false)
# >>> [] and {}
# []
# >>> 3 and []
# []
# ```
# 
# Example2:
# ```python
# X = A or B or C or None  # assigns X to the first nonempty (that is, true) object
# ```
# 
# NOT 
# - ```not x ``` if x is false, then True, else False
# 
# Example:
# ```
# not True # False
# ```
# 
# #### Operator precedences
# 
# - or operator has lower precedense that and operator
# - True and False or True # True
# 
# https://docs.python.org/2/reference/expressions.html#operator-precedence

# In[38]:

a = 3
b = 2.7
c = 'A'
d = [1, 2.1, [1,2], 'python']
e = 'python'
f = (1,2,)
g = {'key1': 1, 'key2': 'two'}
true_or_false = True
no_value_here = None

# define new type
class YourNewType(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b     
your_type_instance = YourNewType(1, 'string')

# define new function
def do_something(param1, param2):
    return param1 * param2
    
function_obj = do_something
value_returned_from_function = do_something(1, 2)
value_returned_from_function = function_obj(1, 2)


# print types and value
print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(f), f)
print(type(g), g)
print(type(true_or_false), true_or_false)
print(type(no_value_here), no_value_here)
print(type(your_type_instance), your_type_instance)
print(type(function_obj), function_obj)
print(type(value_returned_from_function), value_returned_from_function)


# Use http://www.pythontutor.com/ to visualize how Python works. It executes step-by-step all instructions.
# 
# Our example with "Dynamic Types": http://goo.gl/5RTtnU 

# ![example1](example1.png)

# ### Strong Typing
# 
# - the interpreter keeps track of all variables types
# - you can't perform operations inappropriate to the type of the object 
#     - attempting to add numbers to strings will fail
# 

# In[39]:

# Example: 1
a = 3
b = 5
c = a + b

# Example: 2
a = 'A'
b = 'B'
c = a + b

# Example: 3 
[1, 2, 3] + [4, 5]
[1,2, 3] * 3


# In[40]:

# trying to change type

a = 3
b = 'A'
c = a + b


# #### How to "fix" this example?
# 
# Just use one of the available conversion method

# In[41]:

float(2)     # from integer to float 


# In[42]:

int(3.4)     # from float to integer


# In[43]:

str(3)       # from integer to string


# In[44]:

str(4.2)     # from float to integer


# In[45]:

list((1,2,)) # from tuple to list


# In[46]:

# just use one of the conversion method, to convert between types
a = 10
b = "cats"
str(a) + b

# if you want to only print, just print without any conversion
print(a, 'funny', b)


# **Remember**:
# > Don’t check whether it is-a duck: check whether it quacks-like-a duck, walks-like-a duck, etc, etc,
# depending on exactly what subset of duck-like behavior you need to play your language-games with. - (comp.lang.python, Jul. 26, 2000) — Alex Martelli

# In[47]:

help(dir)


# In[48]:

dir(1)


# ### Built-in functions
# 
# - The Python interpreter has a number of functions and types built into it that are always available
# - List of all built-int functions: https://docs.python.org/3/library/functions.html

# In[2]:

import __builtin__   # import builtins - Python 3
dir(__builtin__)


# In[50]:

(1).to_bytes(2, 'big')


# ### The Python Conceptual Hierarchy
# 
# 1. Programs are composed of modules.
# 2. Modules contain statements.
# 3. Statements contain expressions.
# 4. Expressions create and process objects.
# 

# ### Everything in python is an object
# 
# - What is object in general?
# > objects are essentially just pieces of memory, with values and sets of associated operations
# 
# - every object has an identity, a type and a value
# 
# - an object’s identity never changes once it has been created
# - you may think of it as the object’s address in virtual memory
# 
# - the 'is' operator compares the identity of two objects
# 
# - the id() function returns an integer representing its identity
# - in CPython, id() returns the memory address of the object
# 
# https://docs.python.org/3/reference/datamodel.html#objects-values-and-types 

# In[3]:

obj_1 = [1, 2]
obj_2 = [1, 2]

print(id(obj_1))
print(id(obj_2))

print("id(obj_1) == id(obj_2): ", id(obj_1) == id(obj_2))

print("obj_1 == obj_2: ", obj_1 == obj_2)

print("obj_1 is obj_2:", obj_1 is obj_2)


# In[4]:

obj_1 = [1, 2]
obj_2 = obj_1

print(id(obj_1))
print(id(obj_2))

print("id(obj_1) == id(obj_2): ", id(obj_1) == id(obj_2))

print("obj_1 == obj_2: ", obj_1 == obj_2)

print("obj_1 is obj_2:", obj_1 is obj_2)


# **Remember**:
# > The == operator compares the values of objects (the data they hold), while 'is' compares their identities

# ### Python objects - mutables vs immutable
# 
# #### mutable:
#     - mutable objects can change their value but keep their id().
# 
# #### immutable:
#     - an object with a fixed value
#     - immutable objects include numbers, strings and tuples
#     - such an object cannot be altered
#     - a new object has to be created if a different value has to be stored
#     - they play an important role in places where a constant hash value is needed, for example as a key in a dictionary
#     - important advantage - performance
# 
# >knowing that a object is immutable means we can allocate space for it at creation time, 
# and the storage requirements are fixed and unchanging.
# 
# Example: http://goo.gl/N6Rw4P

# In[6]:

# mutable example

l1 = [1, 2, 3]
print(id(l1))

l2 = l1
print(id(l2))

l2.append(4)
print(id(l2))

print(l1)
print(l2)
print(l1 is l2)


# ![mutable-immutable](mutable-immutable.png)

# In[7]:

# immutable example

x = 5
print(id(x))

y = x
print(id(y))

x = x + 1
print(id(x))

print(x)
print(y)
print(x is y)


# ### Data Structures
# 
# Basic data structures (most common used):
# 
# #### lists 
# 
# > [1, 2, 'python', obj1, obj2]
#  
# - sequence type - you can iterate
# - lists are mutable - can be modified in place by assignment to offsets as well as a variety of list method calls
# - can change their value but keep their ID (address in memory) - holds references to objects
# - the list type is a container
# - holds a number of other objects, in a given order
# - no fixed size - they can grow and shrink on demand, in response to list-specific operations like append. remove, ...
# - you can put into list all kind of  objects - list object is the most general sequence
# 
# #### tuples 
# 
# > (1, 2, 'python', obj1, obj2)
#  
# - like a list that cannot be changed 
# - are immutable
# - are used for grouping data
# - cant add/remove elements
# - are faster than list
# - can be used as keys in dictionary
# - functionally, they’re used to represent fixed collections of items
# 
#     
# #### dictionaries
# 
# > {'key1': value1, 'key2': value2}
#    
# - are mutable
# - unordered collection of key-values pairs
# - no duplicate keys
# - implemented using hash table (hash value calculated from the key value)
# - keys shoud be immutable
#     
# #### sets 
# 
# > {1, 2, 'python', obj1, obj2}
# 
# - are mutable
# - unordered collection
# - no duplicate elements
# - implemented using hash table (hash value calculated from the set's item)
# - support mathematical operations: union, intersection, difference, and symmetric difference
# - fast membership testing
# - slower than lists when it comes to iterating over their contents
# 
# - time complexity: https://wiki.python.org/moin/TimeComplexity

# In[55]:

# lists playground

# Example 1: slicing

L = [1, 2, 3, 4, 5, 6]
print(L[1:])
print(L[3:5])
print(L[:-1])
print(L[-1])

# Example 2: memebership checking

print(4 in L)
print(43 in L)

# Example 3: add and remove elements
L.append(7)
L.remove(5)
print(L)

# Example 4: sorting
L.sort()        # sort a list in place, without making a copy, returns None
L2 = sorted(L)  # creates new sorted list and returns it, L list is not sorted


# In[56]:

# Dictionaries plaground
d = {'name': 'James', 'surname': 'Bond', 'code': 7}
name = d['name']
surname = d.get('surname', 'no_name')


# In[6]:

# Sets playground

# Example 1
s1 = {4,3,3,2,1,4,5,1}
print(s1)

# Example 2
s2 = set("abbbbbaaaaacccccddddeeee")
print(s2)

# Example 3
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
print("union: ", set_1 | set_2)
print("intersection: ", set_1 & set_2)
print("difference: ", set_2 - set_1)
print("symetric difference: ", set_1 ^ set_2)


# ### Flow control
# 
# #### if, elif, else
# 
# ```python
# 
# if CONDITION:
#     do something
# elif CONDITION:
#     do something different
# elif CONDITION:
#     do something different
# else:
#      do yet something else
# ```
# 
# #### Loops
# 
# #### for loops
# 
# ```python
# for value in iterable:
#     # do things
# ```
# 
# Example:
# ```python
# items_list = [1, 'A', 'B', 3, [], [1,2,3]]
# for item in items_list:
#     print(item)
# ```
# 
# #### while loops
# 
# ```python
# x = 3
# while x > 0:
#     print(x)  #all the print statement must be in parenthesis for version 3.4.0
#     x = x - 1  #the algebra need not be done within the parenthesis
# ```
# 

# In[58]:

user_input = None
if user_input:
    print(user_input)
elif user_input == 'END':
    print("END")
else:
    print("NO USER INPUT")


# In[8]:

numbers = [1, 2, 3, 4, 5]

number_to_find = 8
print(number_to_find in numbers)

if number_to_find in numbers:
    print("Number {} found in {}".format(number_to_find, numbers))
else:
    print("Cannot find number {} in {}".format(number_to_find, numbers))


# ### Functions
# 
# In simple terms, a function is a device that groups a set of statements so they can be run more than once in a program—a packaged procedure invoked by name. Functions also can compute a result value and let us specify parameters that serve as function inputs and may differ each time the code is run.
# 
# ```python
# 
# def function(arguments):
#     # do something
#     return 
# ```

# In[10]:

def add_numbers(num1, num2):
    return num1 + num2

number = add_numbers(1, 2)
print number


# In[11]:

def add_numbers(*numbers):
    return sum(numbers)

print("1 + 2 = ", add_numbers(1, 2))
print("1 + 2 + 3 = ", add_numbers(1, 2, 3))
print("1 + 2 + 3 + 4 = ", add_numbers(1, 2, 3, 4))


# In[11]:

def multiple_params_test(param1=None, param2=0, *args, **kwargs):
    if kwargs.get('param', None):
        pass
    print(param1)
    print(param2)
    print(args)
    print(kwargs)
    #print(param1, param2, args, kwargs)
    
multiple_params_test(1, 2, 3, 4, 5, param3=3, param4=4)


# In[63]:

def add_numbers(a=0, b=0, c=None):  # default values for attributes
    """
    Function add numbers
    """
    if c:
        pass
    return a + b

print(add_numbers())
print(add_numbers(2, 2))


# ### Functions in Python are first-class objects
# 
# - created at runtime
# - assigned to a variable or element in a data structure
# - passed as an argument to a function
# - returned as the result of a function
# 
# - integers, strings, and dictionaries are other examples of first-class objects in Python

# In[64]:

def do_something(param1):
    return param1

# remember: functions are object
print("function name: ", do_something.__name__)

value_returned_by_function = do_something(param1=1) # call function

function_object = do_something # Notice: there is no braces '()', just function name
dir(function_object)

objects_storage = [1, 'python', do_something, function_object]

for obj in objects_storage:
    print(obj)


# In[65]:

dir(do_something)


# In[66]:

def print_a(): print('a')
def print_b(): print('b')
def print_c(): print('c')
    
function_storage = [print_a, print_b, print_c]

for fn in function_storage:
    fn()  # run each function from 'function_storage' list


# In[67]:

def run_function(function):
    return function()
    
def function_to_run(): print("do something")
    
run_function(function_to_run)


# In[68]:

# swtich

user_actions = {
    'click_button_a': print_a,
    'click_button_b': print_b,
    'click_button_c': print_c}

user_choose = 'click_button_a'

user_actions[user_choose]()


# ### Function parameters: call by value or by reference?
# 
# - it is called “object reference” or "by sharing"
# 
# - call by sharing means that each formal parameter of the function gets a copy of each reference in the arguments
# - the parameters inside the function become aliases of the actual arguments
# 
# - the result of this scheme is that a function may change any mutable object passed as a parameter
# - but it cannot change the identity of those objects (i.e., it cannot altogether replace an object with another).
# 
# - best example: http://goo.gl/uWjZuT
# 
# - good explanation:
# - http://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/ 
# - http://effbot.org/zone/call-by-object.htm
# - https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/

# In[69]:

def f(a, b):
    a = a + b
    return a    

x = [1,2]
y = [3,4]
result = f(x, y)
print("result: ", result)

# what happend with x value?
print(x)
print(y)


# ![example3](example2.png)

# How to "fix" this? What you should do to keep this x list without modification?

# In[70]:

def f(a, b):
    new_obj_a = a
    new_obj_b = b
    
    new_obj_a = new_obj_a + new_obj_b
    return new_obj_a

x = [1,2]
y = [3,4]
result = f(x, y)
print("result: ", result)

# what happend with x value?
print(x)
print(y)


# ![example3](example3.png)

# In[71]:

def f(a, b):
    new_obj_a = a[:]
    new_obj_b = b[:]
    a.append(2)
    new_obj_a = new_obj_a + new_obj_b
    return new_obj_a

x = [1,2]
y = [3,4]
result = f(x, y)

# http://goo.gl/VO153U 


# ![example4](example4.png)

# ### Copying objects in Python
# 
# - copies are shallow by default!
# 
# - using the constructor or [:] produces a shallow copy 
# - the copy is filled with references to the same items held by the original container
# - this saves memory and causes no problems if all the items are immutable
# - if there are mutable items, this may lead to unpleasant surprises
# 
# 
# * Example 1: http://goo.gl/P3wj4O
# * Example 2: http://goo.gl/nIOz1U

# In[17]:

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)

print("AFTER COPY:")
print('l1:', l1)
print('l2:', l2)


print("\nAFTER L1 updates:")
l1.append(100) 
l1[1].remove(55)

print('l1:', l1)
print('l2:', l2)


print("\nAFTER L2 updates:")

l2[1] += [33, 22]
l2[2] += (10, 11)


print('l1:', l1)
print('l2:', l2)


# ![example5](example5.png)

# In[19]:

# Solution is to use deepcopy

from copy import deepcopy

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = deepcopy(l1)

print("AFTER COPY:")
print('l1:', l1)
print('l2:', l2)


print("\nAFTER L1 updates:")
l1.append(100) 
l1[1].remove(55)

print('l1:', l1)
print('l2:', l2)


print("\nAFTER L2 updates:")

l2[1] += [33, 22]
l2[2] += (10, 11)


print('l1:', l1)
print('l2:', l2)


# ### Reading and writing files
# 
# We have four basic operations:
# 
# - Open
#     - returns a file object
#     - open modes: r (read), w (write), r+ (read and write), a (append)
#     
# ```python
# f = open('filename', 'r+')
# ```
# 
# - Read
#     - read strings from file
#     - open returns file object (interator) so we can use file object like sequence
# 
# Example 1:
# ```python
# f = open('filename', 'r')
# f.read()
# f.close()
# ```
# 
# Example 2:
# ```python
# f = open('filename', 'r')
# for line in f:
#     print line
# ```
# 
# - Write
# 
# ```python
# f = open('filename', 'w')
# f.write('first line\n')
# f.close()
# ```
# 
# - Close
#     - close and free up any system resources taken up by the open file
#     - file object cannot be used after closing operation

# In[73]:

f = open('file_to_write', 'w')

print('f.mode   ->', f.mode)      # access mode
print('f.closed ->', f.closed)    # is file closed
print('f.name   ->', f.name)      # file name

f.close()
print('-> closing file')
print('f.close  ->', f.closed)    # is file closed


# In[74]:

# Example: writing to file

# need to open file -> open(file_name, mode)
f = open('test_file', 'w')

f.write('write first line to file\n')
f.write('write second line to file\n')

# writelines expects a list of strings, while write expects a single string

save_to_file = [
    'third line\n',
    'fourth line \n'
]

f.writelines(save_to_file)

# remember to close file
f.close()


# In[75]:

# Example: reading from file

f = open('test_file', 'r')

print(f.read())

f.close()


# In[76]:

# Example: reading from file using for loop

f = open('test_file', 'r')
for line in f:
    print(line)


# In[77]:

# Ezample: context managers for handling file I/O operations

with open('test_file', 'w') as f:
    f.write('one\n')
    f.write('two\n')
    
with open('test_file', 'r') as f:
    print(f.read())


# ### Exceptions
# 
# > Easier to ask for forgiveness than permission
# 
# #### What is exception?
# - events that can modify the flow of control through a program
# - are triggered automatically on errors
# - what is error?
#     - syntax error -> parsing error, syntactically incorrect
#     - exception - statement or expression syntactically correct, errors detecting during execution
# 
# 
# #### How to handle with exceptions?
# 
# - Use try/except block to catch and recover from exceptions 
# ```python
# try:
#     # code that will break (will throw exception)
#     x = 1/0
# except EXCEPTION as E:
#     #do something with exception
#     print E
# ```
# 
# - Use try/finally block to perform cleanup actions, whether exception occurs or not
# ```python
# try:
#     f = open('file', 'r')
#     # do something with file
# finally:
#     f.close()  # always invoke close
# ```
# 
# - Use raise statement to raise exception manually
# ```python
# raise RuntimeError()
# ```
# 
# #### Built-in Exceptions (most common)
# 
# - ImportError -> raised when an import statement fails to find the module definition
# - IndexError  -> raised when a sequence subscript is out of range, e.g: index[1000]
# - StopIteration -> signal that there are no further items produced by the iterator e.g: for loop
# - SyntaxError -> raised when the parser encounters a syntax error
# - IOError -> raised when input or output fails, for example if a disk fills up or an input file does not exist
# - KeyError -> raised when a value is not found as a key of a dictionary
# 
# #### Assertions
# 
# - used to verify program conditions during development
# - assert statements may be removed from a compiled program’s byte code - need to execute python program with -O flag
# 
# ```python
# def f(x):
#     assert x < 0, 'x must be negative' # if not it will raise AssertionError
#     return x ** 2
# ```
# 
# 
# Source:
# - https://docs.python.org/3/tutorial/errors.html
# - https://docs.python.org/3/library/exceptions.html
# - https://pymotw.com/2/exceptions/

# In[18]:

try:
    import module_does_not_exist
except ImportError as exc:
    print("Cannot find such module")
    import math


# In[20]:

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # We have 10 elements in this list
try:
 print(numbers[11]) # ask for 11th element
except IndexError:
    print("error")


# In[80]:

my_dictionary = {
    'key_one': 1,
    'key_two': 2,
}

my_dictionary['key_one'] # prints 1
my_dictionary['key_two'] # prints 2
my_dictionary['key_not_exist'] # error


# In[81]:

try:
    x = 1/0
except ZeroDivisionError as err:
    print(err)


# In[82]:

raise ZeroDivisionError('division by zero, oh no!')


# In[83]:

try:
    raise ZeroDivisionError('division by zero, oh no!')
except ZeroDivisionError as err:
    print(err)


# In[84]:

f = open("not_exist", 'r')


# In[85]:

try:
    f = open("not_exist", 'r')
except FileNotFoundError as err:
    print("File not found:", err)
except IOError as err:
    print("IOError:", err)
finally:
    print("Finally executed")
    f.close()


# In[86]:

def fn():
    try:
        return
        print(1)
    except:
        pass
    finally:
        print("finally")
        
fn()


# ### Modules
# 
# - Every file of Python source code whose name ends in a .py extension is a module
# - Other files can access the items a module defines by importing that module
# - Import operation essentially loads another file (module)
#     - imports must find files, compile them to byte code, and run the code
# 
# - More specifically, modules have at least three roles:
# 1. Code reuse
# 2. System namespace partitioning
# 3. Implementing shared services or data (e.g: global object)
# 
# > modules provide an easy way to organize components into a system by serving as self-contained packages of variables known as namespaces
# 
# 
# #### Import operation
# 
# - Import operations essentially load another file and grant access to that file’s contents
# - Python searches for imported modules in every directory listed in sys.path
# 
# > imports are not just textual insertions of one file into another. They are really runtime operations that perform three distinct steps the first time a program imports a given file:
# Python does this by storing loaded modules in a table named sys.modules and checking there at the start of an import operation. If the module is not present, a three-step process begins:
# 1. Find the module’s file.
# 2. Compile it to byte code (if needed).
# 3. Run the module’s code to build the objects it defines.
# 
# 
# ##### Import search path
# 
# The Module Search Path:
# 1. The home directory of the program (automatic)
# 2. PYTHONPATH directories (if set)
# 3. Standard library directories
# 4. The contents of any .pth files (if present)
# 5. The site-packages home of third-party extensions
# 
#     
# ##### Python modules - examples:
# 
# - my_lib.py
# 
# ```python
# 
# ATTRIBUTE_ONE = "attribute_one"
# LIST_OF_NUMBERS = [1, 2, 3, 4]
# 
# def do_something(*args):
#     return *args
#     
# def do_something_complicated(*args):
#     return 2 + 2
#     
# if __name__ == "__main__":
#     do_something(1, 2, 3)
# 
# ```
# 
# - my_script.py
# 
# ```python
# 
# from my_lib import do_something
# 
# do_something(5, 6, 7)
# 
# print my_lib.ATTRIBUTE_ONE
# ```

# In[87]:

import collections

from collections import OrderedDict

from collections import OrderedDict as ordered_dict


# In[88]:

import math

from imp import reload
reload(math)


# In[89]:

from A import func
from B import func             # This overwrites function we fetched from A
func()                         # It calls A.func() only

# How to fix this?

from A import func as afunc    # Rename uniquely with "as"
from B import func as bfunc
afunc()
bfunc()               


# ### Garbage collector
# 
# Python has a feature known as garbage collection that cleans up unused memory as your program runs and frees you from having to manage such details in your code.
# 
# 
# - When we lose the last reference to the object by assigning its variable to something else, all of the memory space occupied by that object’s structure is automatically cleaned up for us
# 
# - Technically speaking, Python’s garbage collection is based mainly upon reference counters
# 
# 
# ##### How to check pointers to object (number of references)?
# 
# ```python
# >>> import sys
# >>> sys.getrefcount(1)    # 647 pointers to this shared piece of memory
# ```
# 

# ### Better to know ...
# 
# - Python cannot run programms in parallel - there is a global mutex (Global Interperer Lock)
# - GIL ensures that only one thread runs in the interperter at once
# - sources:
#     - https://wiki.python.org/moin/GlobalInterpreterLock
#     - http://www.dabeaz.com/python/UnderstandingGIL.pdf
# - we have GIL only in CPython implementaion
#     - you can use others python implemention: Jython, IronPython, PyPy
#     

# ### How to learn Python?
# 
# 
# - first, master the fundamentals
# 
# - python official documentation: https://docs.python.org/3/
# - well writen python tutorial: https://docs.python.org/3/tutorial/index.html 
# - coding standard, style guide - pep8: https://www.python.org/dev/peps/pep-0008/ 
# - visualize execution of code: http://www.pythontutor.com/

# In[90]:

import this


# ### Fetching data from web
# 
# > The Requests package is recommended for a higher-level http client interface
# 
# > Requests allow you to send HTTP/1.1 requests. You can add headers, form data, multipart files, and parameters with simple Python dictionaries, and access the response data in the same way. It’s powered by httplib and urllib3
# 
# - Remember to install requests package, because it is 3rd party library
# 
# ```bash
# pip install requests
# ```
# 
# Sources:
# - https://docs.python.org/2/library/urllib.html
# - http://docs.python-requests.org/en/master/

# In[91]:

import requests
r = requests.get('https://api.github.com/events')
r.content


# #### For advanced users
# 
# - python enhancement proposals: https://www.python.org/dev/peps/ 
# - let's look into Full Python Grammar specification: https://docs.python.org/3.1/reference/grammar.html
# - python official repository: https://hg.python.org/
# 

# ### How to install 3rd party libraries
# 
# - PyPI - the Python Package Index (repository of python non-standard libraries), currently ~ 75 k libraries
# - to install additional libraries you need to use additional program:
#     - easy_install - very basic lib installer
#     - pip - is the preferred installer program
#     
# Examples:
# ```bash
# $ pip install SomePackage
# ```
# 
# ```bash
# python -m pip install SomePackage
# ```
# 
# ```bash
# pip install SomePackage==1.0.4    # specific version
# ```
# 
# ```bash
# $ pip show --files SomePackage
#   Name: SomePackage
#   Version: 1.0
#   Location: /my/env/lib/pythonx.x/site-packages
#   Files:
#    ../somepackage/__init__.py
#    [...]
# ```
# 
# Sources:
# - https://pypi.python.org/pypi/pip
# - https://docs.python.org/dev/installing/
# - https://pypi.python.org/pypi
# - https://pip.pypa.io/en/stable/installing/
# - http://python-packaging-user-guide.readthedocs.org/en/latest/pip_easy_install/

# ### Virtual environments
# 
# > a virtual environment is a semi-isolated Python environment that allows packages to be installed for use by a particular application, rather than being installed system wide
# 
# 
# Steps to create virtual environment:
# - Install virtual environment
# ```
# $ pip install virtualenv
# ```
# 
# - Create a virtual environment for a project
# 
# ```
# $ mkdir lab_env
# $ cd lab_env
# $ virtualenv lab_env 
# ```
# 
# - You can use your virtual python interpreter
# 
# ```
# $ source venv/bin/activate
# (lab_env) $ pip install requests
# ```
# 
# 
# Sources:
# - http://docs.python-guide.org/en/latest/dev/virtualenvs/

# ### Scopes - local vs global
# 
# ```python
# X = 1 # Global scope
# 
# def fn1():  # Local scope inside function fn1
#     X = 2
#     fn1 = 1
#     
# def fn2():  # Local scope inside function fn2
#     X = 3
#     fn2 = 3
# 
# # Global scope
# 
# Y = 3 
# fn1 = fn1()
# fn2 = fn2()
# 
# ```
# 
# #### Scope
# - The places where variables are defined and looked up
# - Help prevent name clashes across your program’s code
# 
# - Names assigned inside a def can only be seen by the code within that def
# - Names assigned inside a def do not clash with variables outside the def, even if the same names are used elsewhere
# 
# - If a variable is assigned inside a def, it is local to that function.
# - If a variable is assigned outside all defs, it is global to the entire file
# 
# #### Scopes in Python
# 
# local namespace 
#     - specific to the current function or class method. If the function defines a local variable x, or has an argument x, Python will use this and stop searching.
# 
# global namespace 
#     - specific to the current module. If the module has defined a variable, function, or class called x, Python will use that and stop searching.
# 
# built-in namespace 
#     - global to all modules. As a last resort, Python will assume that x is the name of built-in function or variable.
# 
# #### Global
# 
# - By default, all names assigned in a function are local to that function
# - Global declares module-level variables that are to be assigned
# - Global names are variables assigned at the top level of the enclosing module file
# 
# - "global" statement tells that a function plans to change one or more global names

# In[92]:

X = 1 # Global scope

def fn1():  # Local scope inside function fn1
    X = 2
    fn1 = 1
    
def fn2():  # Local scope inside function fn2
    X = 3
    fn2 = 3

# Global scope

Y = 3 
fn1 = fn1()


# In[93]:

# locals() functions returns all names from local scope

def print_locals():
    a = 1
    b = 2
    print(locals())
    
print_locals()


# In[94]:

# __builtins__ in Python 2.x

import builtins # in Python 3.x
dir(builtins)


# In[1]:

# Trap !

def trap():
    print = "Print something"   # Redefine built-in name "print"
    print("function local scope")

print("module global scope")
trap()




# In[5]:

# in Python 2.X you could say __builtin__.True = False, to reset True to False for the entire Python process

print bool(1)

True = False

if True:
    print "a"



# In[ ]:

X = 1       # Global scope

def increment():
    X = 3  # Local scope - inside function
    X = X + 1
    print('X inside function: ', X)

increment()
print('X outside function:', X)


# In[ ]:

X = 1       # Global scope
def increment():
    X = X + 1      # UnboundLocalError: local variable 'X' referenced before assignment
    print('X inside function: ', X)

increment()
print('X outside function:', X)


# In[ ]:

X = 1
def increment():
    global X      #  we are using X from global scope
    X = X + 1
    print('X inside function: ', X)

increment()
print('X outside function:', X)


# In[ ]:

# Global scope
X = 99                # X and func assigned in module: global

def func(Y):          # Y and Z assigned in function: locals
    # Local scope
    Z = X + Y         # X is a global
    return Z

func(1)               # func in module: result=100


# In[ ]:

X = 99                   # Global scope name: not used

def f1():
    X = 88               # Enclosing def local
    def f2():
        print(X)         # Reference made in nested def
    f2()

f1()               


# ### Creating own types - classes
# 
# #### Class
# 
# - A user-defined prototype for an object that defines a set of attributes that characterize any object of the class
# - The attributes are data members (class variables and instance variables) and methods, accessed via dot notation
# - Simply speaking: A coding structure used to implement new kinds of objects in Python
# - Classes are a kind of factory for generating instances
# - Classes are created with a new statement: the ```class```
# 
# ```python
# class MyClass:
#     #class body
# ```
# 
# 
# #### Class variable
# 
# - A variable that is shared by all instances of a class
# - Class variables are defined within a class but outside any of the class's methods
# - Class variables aren't used as frequently as instance variables are
# 
# ```python
# class MyClass:
#     shared_value = 100
#     
# MyClass.shared_value
# ```
# 
# 
# #### Data member
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# - A class variable or instance variable that holds data associated with a class and its objects
# 
# ```python
# class MyClass:
#     shared_value = 100
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         
#     def get_a(self):
#         return self.a
# ```
# 
# 
# #### Function overloading
# 
# - The assignment of more than one behavior to a particular function
# - The operation performed varies by the types of objects (arguments) involved
# 
# ```python
# class MyClass:
# 
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         
#     def __init__(self, a, b, c): # python will invoke only this method
#         self.a = a
#         self.b = b
#         self.c = c
# 
# ```
# 
# #### Instance variable (attribute)
# 
# - A variable that is defined inside a method and belongs only to the current instance of a class
# - Assignments inside class statements make class attributes
# 
# ```python
# 
# class MyClass:
# 
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
# 
# obj = MyClass(1, 2)
# obj.a
# obj.__dict__['a'] 
# ```
# 
# 
# 
# #### Inheritance
# 
# - The transfer of the characteristics of a class to other classes that are derived from it
# - Inheritance is based on attribute lookup in Python (in X.name expressions)
# - Multiple inheritance allowed (class may have more than one superclass above it in the class tree)
# 
# Key ideas:
# - Superclasses are listed in parentheses in a class header e.g MyClass(A, B, C)
# - Classes inherit attributes from their superclasses
# - Instances inherit attributes from all accessible classes
# 
# ```python
# class A(object):
#     pass
#     
# class B(A):
#     pass
# 
# ```
# 
# #### Instance
# 
# - An individual object of a certain class
# - Instance objects are concrete items
# - Calling a class object like a function makes a new instance object
# - Each instance object inherits class attributes and gets its own namespace
# - Assignments to attributes of self in methods make per-instance attributes
# 
# ```python
# my_class_obj = MyClass(1, 2)
# 
# my_class_obj.new_attribute = 3  # create (assign) new attribute to this particular instance only
# 
# ```
# 
# 
# #### Instantiation
# 
# - The creation of an instance of a class
# 
# 
# #### Method
# 
# - A special kind of function that is defined in a class definition
# 
# ```python
# class MyClass:
# 
#     def method_1(self, a, b):
#         print(a, b)
#         
#     def method_2(self, a, b, c):
#         print(a, b, c)
# ```
# 
# 
# #### Object
# 
# - A unique instance of a data structure that's defined by its class
# - An object comprises both data members (class variables and instance variables) and methods
# 
# 
# #### Operator overloading
# 
# - The assignment of more than one function to a particular operator
# 
# 
# Sources:
# - https://docs.python.org/2/tutorial/classes.html

# In[42]:

class Person(object):
    label = 'Person'
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def name_surname(self):
        print "iside method", self.name + " " + self.surname
      
    
    def __str__(self):
        return self.name + " " + self.surname
    
    def __eq__(self, other):
        return self.name > other.name
    
    def __hash__(self):
        return hash(self.name)
    
        

p = Person(name="Guido", surname="Van Rossum")
print(p.name)
print(p.surname)
print(p.label)
print(Person.label)

p.name_surname()

print p


#print(p.__dict__['name'])


# In[43]:

p1 = Person(name="Guido", surname="Van Rossum")
p2 = Person(name="Maciej", surname="Python")

p1 > p2

s = set([p1, p2])
print s


# ### Privacy
# 
# - In Python, there is no way to create private variables like there is with the private modifier in Java
# - What we have in Python is a simple mechanism to prevent accidental overwriting of a “private” attribute

# In[26]:

class Employer(object):
    def __init__(self, bonus):
        self.job_grade = 10
        self.salary = 1500 + (bonus * self.job_grade)

employer_1 = Employer(bonus=1500)
print employer_1.salary
#employer_1.job_grade = 100
print("job grade :", employer_1.job_grade)

#print employer_1.__salary 

#print("salary    :", employer_1.__salary)


# In[19]:

print dir(employer_1)
salary = employer_1._Employer__salary
print(salary)


# ### Special methods
# 
# - Methods named with double underscores (__X__) are special hooks
# - Such methods are called automatically when instances appear in built-in operations
#     - Special methods are meant to be called by the Python interpreter, and not by you
#     - Don't write obj.\__len\__(), but len(obj) - Python will call \__len\__() method behind the scenes
# - Classes may override most built-in type operations
# 
# Some examples:
# 
# * \__init\__()
# * \__new\__()
# * \__repr\__()
# * \__len\__()
# * \__str\__()
# * \__eq\__()
# * \__hash\__()
# * \__getitem\__()
# * \__add\__()
# 
# and many many more. Visit http://www.rafekettler.com/magicmethods.html to get more information.

# In[ ]:

class NewStyle(object): pass
class OldStyle: pass


# In[ ]:

class Employee(object):
    static_counter = 0
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.salary = 1500
        self.__job_grade = 1
        Employee.static_counter += 1
    
    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary
    
    def __str__(self):
        return "{name}{surname} get {salary} PLN".format(
            name=self.name, surname=self.surname, salary=self.salary)
    
    @classmethod
    def get_counter(cls):
        return cls.static_counter
    
  
employee = Employee('Lucky', 'Boy')

employee.name = "a"
employee.surname = "b"
employee.new_attribute = "new attribute"

print(employee.new_attribute)

print(employee.get_name())

print(employee.get_salary())

print(employee)

print(employee.get_counter())

print(Employee.get_counter())


# In[ ]:

class B(object): pass

class A(object):
    def __init__(self): # first init
        print("A")
    def __init__(self): # second init
        print("B")

a = A()  # second init was used


# In[ ]:

class Figure(object):
    __slots__ = ['width', 'height']

f = Figure()
f.width = 10
print(f.width)

f.size = 10  # AttributeError: 'Figure' object has no attribute 'size'


# In[ ]:

# Class inheritance

class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species 
    def get_name(self):
        return self.name
    def get_species(self):
        return self.species
    
class Dog(Pet):
    def __init__(self, name, hates_cat=True):
        Pet.__init__(self, name, 'Dog')
        #super(Dog, self).__init__(name, 'Dog')
        self.hates_cat = hates_cat
    def hates_cat(self):
        return self.hates_cat
    def get_species(self):
        return 'Doggggg'
    
pet = Pet('Mister', 'Cat')
print(pet.get_species())

dog = Dog('Mister', hates_cat=True)
print(dog.get_species())


# In[ ]:




# In[ ]:

text = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
"""

import re # find more information here: https://docs.python.org/2/library/re.html 

regex = re.compile('^\w+', re.MULTILINE) # regular expression

class TextFilter(object):
    def __init__(self, text): 
        self.words = regex.findall(text)
    def __getitem__(self, index):
        return self.words[index]
    def __repr__(self):
        return str(self.words)
    def __len__(self):
        return len(self.words)

filtered_text = TextFilter(text)

print(filtered_text)
print("number of list elements: ", len(filtered_text))
print("word in list: ", 'Simple' in filtered_text)
print("slicing: ", filtered_text[2:4])

for word in filtered_text:
    print(word)


# In[ ]:

# We can do it even much simpler ...

filtered_text = regex.findall(text)
print(filtered_text)


# In[ ]:



