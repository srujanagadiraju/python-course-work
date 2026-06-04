Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=' hello world  '
>>> s
' hello world  '
>>> s.strip()
'hello world'
>>> s.lstrip()
'hello world  '
>>> s.rstrip()
' hello world'
>>> 
===================================== RESTART: Shell =====================================
>>> s='strings.py'
>>> s
'strings.py'
>>> s.startswith('str')
True
>>> s.startswith('gfh')
False
>>> s.endswith('py')
True
>>> s.endswith('js')
False
>>> 'hgtfd'.isalpha()
True
>>> 'HFTGHJ'.isalpha()
True
>>> 'hjhJH12'.isalpha()
False
>>> 'jgk@kj'.isalpha()
False
