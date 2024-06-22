
## What does ** (double star/asterisk) and * (star/asterisk) do for parameters?
# The *args will give you all positional arguments as a tuple:
# The **kwargs will give you all keyword arguments as a dictionary:
# * (tuple) :-  *unlimited_arguments  (6, 'tester', 1, 2, 3, 4, 5)
# ** (dict) :-  **unlimited_keyword  {'e': 3, 'checker': 1, 'd': 'keyvalue', 'name': 'my_name'}
# Summary
# *args in function definitions collects extra positional arguments as a tuple.
# * in function calls unpacks an iterable into positional arguments.
# * in function definitions can also enforce keyword-only arguments.  
# **kwargs in function definitions collects extra keyword arguments as a dictionary.       
# ** in function calls unpacks a dictionary into keyword arguments.
## *arg and **args         

def foo(x, y, *args):
    pass

def bar(x, y, **kwargs):
    pass


##===========================================================================================================================##

print('\n Single Asterisk * ')
# Single Asterisk * 
#1- Positional Arguments: *args allows a function to accept any number of positional arguments.

def foo(*args):
    for arg in args:
        print(arg)

foo(1, 2, 3)
# Output:
# 1
# 2
# 3

# 2- In Function Calls:
# Unpacking Iterables: * can unpack iterables into positional arguments.
def bar(a, b, c):
    print(a, b, c)

elements = [1, 2, 3]
bar(*elements)
# Output:
# 1 2 3

# 3- Keyword-Only Arguments:
# Separator: * can indicate that subsequent parameters must be specified as keyword arguments.
def baz(a, b, *, c, d):
    print(a, b, c, d)

baz(1, 2, c=3, d=4)
# Output:
# 1 2 3 4

print('\n Double Asterisk ** ')
#Double Asterisk **
# 1- In Function Definitions:
# Keyword Arguments: **kwargs allows a function to accept any number of keyword arguments.
def foo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

foo(a=1, b=2)
# Output:
# a = 1
# b = 2

# 2- In Function Calls:
# Unpacking Dictionaries: ** can unpack a dictionary into keyword arguments.
def bar(a, b, c):
    print(a, b, c)

elements = {'a': 1, 'b': 2, 'c': 3}
bar(**elements)
# Output:
# 1 2 3


##===========================================================================================================================##

print('\n10 class Python Crash Course | functions, lambda, decorators, recursive, generator, *arg and **args ')
## pytonclass
# new way, # passing through positional argument
# first value goes in 1st and sendon value goes to 2nd position

print('\npositional argument, position is important ')
def add_two_num(num1:int, num2:int) -> int:
    print(f"num1 value {num1} and num2 value {num2}")
    return num1 + num2
print(f'positional argument {add_two_num(3,4)}')   # call function
# output :- positional argument 7

# key word arguments (get it from name, not need to predefine)
print('\nkey word argument, value get it by name ')
def add_two_num(num1:int, num2:int) -> int:
    print(f'num1 value {num1} and num2 value {num2}')
    return num1 + num2
print(f'key word arguments {add_two_num(num2=3, num1=2)}')  # call function

# pass unlimated key words arguments ( ** ) return dictionary (time 1:30)
# note:- we havn't pass any variable in function
print('\nunlimited keyword arguments (**) return dictionary ')
def unlimited_keyword_arguments(**karguments):    
    print(karguments, type(karguments))

unlimited_keyword_arguments(x=2, c=20, a='letter', name="Mike")   # call function
# output :- {'x': 2, 'c': 20, 'a': 'letter', 'name': 'Mike'} <class 'dict'>

# time 1:32 (43)
print('\nexample:- unlimited arugument / keywords')
print(f'required_variable (a), unlimited_comma_seprated_arguments(*), unlimited_keyword_arguments(**)')

def test_function(a, *unlimited_arguments, **unlimited_keyword):
    print(f''' required_any_variable {a},
          *unlimited_arguments  {unlimited_arguments},
          **unlimited_keyword  {unlimited_keyword}
          ''')
    
test_function(123, 6, 'tester', 1,2,3,4,5, e=3, checker=1, d='keyvalue', name='my_name')

print(f'\nexample: define type')

def test_function(a, b:int, c:str, *unlim_arg : Tuple[int,...] , **unlim_keyword : Dict[str,int]) -> None:
    print(f''' required_any_variable {a}, require_int {b}, require_str {c},
          *unlimited_arguments  {unlim_arg},
          **unlimited_keyword  {unlim_keyword}
          ''')
    
test_function(678, 7, 'test_type', 6,7,8,9,10, e=3, tester=1, d=40)

# typing not require
print('\nexample: typing is not require because * (tuple) , ** (dict)')
def my_function(a:int, b:int, *unlimit_arg:int, **unlimit_keyword: int) -> None:
    print(a,b, unlimit_arg, unlimit_keyword)

my_function(1,2, 7,9,9,9, c=20, d= 30, x=100)
# output :- 1 2 (7, 9, 9, 9) {'c': 20, 'd': 30, 'x': 100}




