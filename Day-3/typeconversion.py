Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> a
10
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> str(a)
'10'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> bool(0)
False
>>> b=10.5
>>> int(b)
10
>>> complex(b)
(10.5+0j)
>>> str(b)
'10.5'
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
bool(b)
True
bool(0.0)
False
c=2+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
str(c)
'(2+3j)'
bool(c)
True
s='python'
a='456985'
b='345667.45'
int(s)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
int(a)
456985
int(b)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '345667.45'
float(a)
456985.0
float(b)
345667.45
list(a)
['4', '5', '6', '9', '8', '5']
list(s)
['p', 'y', 't', 'h', 'o', 'n']
list(b)
['3', '4', '5', '6', '6', '7', '.', '4', '5']
tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
set(s)
{'y', 'o', 'p', 't', 'n', 'h'}
bool(s)
True
complex(a)
(456985+0j)
(456789+0j)
(456789+0j)
complex(b)
(345667.45+0j)
l=[1,2,3,4,5,6,7,8]
l
[1, 2, 3, 4, 5, 6, 7, 8]
int(l)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
