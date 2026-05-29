Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> type(a)
<class 'int'>
>>> a=99.9
>>> type(a)
<class 'float'>
>>> a=12+8j
>>> type(a)
<class 'complex'>
>>> s='era'
>>> type(s)
<class 'str'>
>>> s=''era''
SyntaxError: invalid syntax
>>> s="era"
>>> type(s)
<class 'str'>
>>> s='''era'''
>>> type(s)
<class 'str'>
>>> l=[1,2,3,4]
>>> type(l)
<class 'list'>
>>> l=[]
>>> l=list()
>>> type(l)
<class 'list'>
>>> t=()
>>> t=(1,34,5,6)
>>> t
(1, 34, 5, 6)
>>> type(t)
<class 'tuple'>
>>> s=[1,2,3,7,8]
>>> type(s)
<class 'list'>
>>> s=set()
>>> s=[4567,5678,7890]
>>> a=10
>>> type(s)
<class 'list'>
