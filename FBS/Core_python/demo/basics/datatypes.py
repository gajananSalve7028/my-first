####1. numeric
#1. int

#int var #variable declaration
var = 10   #variable initilization

print(type(var))

#2. float
var = 3.14

#3. complex
var = 10+5j #real+imaginary




####2. text
#str
var='first"bit" solution'
var="firstbit's solution"
var='''this is first line.
this is second line.'''
"""name:datatypes.py
author.gajanan salve
date:05.05.2005"""

print(type(var))


####3. sequential
#1. list
var=[10,20,30,40]

#2. tuple
var=(10,20,30,40)

#3. range()
var=range(1,51)


####4. set type
#1. set 
var={10,20,30,40}

#2. frozenset
var=({10,20,30,40})


####5. mapping
#1. dict
var={1:'python',2:'java',3:'c++'}

####6. other
#1. boolean
var = True

#2. nonetype
var = None

print(type(var))
