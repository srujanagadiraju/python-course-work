Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['demo']='str'
d
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d[False]='bool'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex', False: 'bool'}
d=
SyntaxError: invalid syntax
d={}
d=[1]=1
SyntaxError: cannot assign to literal
d={}
d=[1]=1
SyntaxError: cannot assign to literal
d[1]=1
d
{1: 1}
d[23]=23.4
d[3]='fghjk'
d[4]=3+4j
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]={1,3}
d[8]={1:1,2:2]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
d[8]={1:1,2:2}
d
{1: 1, 23: 23.4, 3: 'fghjk', 4: (3+4j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 1, 2: 2}}
d[1]=14
d
{1: 14, 23: 23.4, 3: 'fghjk', 4: (3+4j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 1, 2: 2}}
d={}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:4,3:6,4:8,5:10,6:12}
d[14]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    d[14]
KeyError: 14
d[4]
8
d[6]
12
d[1]
2
d={'srujana':89,'rishi':76,'veda':90,'sai':50}
d
{'srujana': 89, 'rishi': 76, 'veda': 90, 'sai': 50}
d['srujana']
89
d['rishi']
76
d['veda']
90
d['sai']
50
d['baba']
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    d['baba']
KeyError: 'baba'
d.get('baba')
d.get('subbu')
d.get('sai')
50
d.get('baba','user not found')
'user not found'
d.get('sai','user not found')
50
d
{'srujana': 89, 'rishi': 76, 'veda': 90, 'sai': 50}
'srujana' in d
True
'veda' in d
True
'subbu' not in d
True
d.keys()
dict_keys(['srujana', 'rishi', 'veda', 'sai'])
d.values()
dict_values([89, 76, 90, 50])
d.items()
dict_items([('srujana', 89), ('rishi', 76), ('veda', 90), ('sai', 50)])
sorted(d)
['rishi', 'sai', 'srujana', 'veda']
max(d)
'veda'
max(d)
'veda'
>>> min(d)
'rishi'
>>> len(d)
4
>>> d['sai']
50
>>> d['sai']=100
>>> d
{'srujana': 89, 'rishi': 76, 'veda': 90, 'sai': 100}
>>> d['veda']=70
>>> d
{'srujana': 89, 'rishi': 76, 'veda': 70, 'sai': 100}
>>> d['subbu']=60
>>> d
{'srujana': 89, 'rishi': 76, 'veda': 70, 'sai': 100, 'subbu': 60}
>>> d.update({'baba':20})
>>> d
{'srujana': 89, 'rishi': 76, 'veda': 70, 'sai': 100, 'subbu': 60, 'baba': 20}
>>> d.popitem()
('baba', 20)
>>> d
{'srujana': 89, 'rishi': 76, 'veda': 70, 'sai': 100, 'subbu': 60}
>>> d
{'srujana': 89, 'rishi': 76, 'veda': 70, 'sai': 100, 'subbu': 60}
>>> d.pop('subbu':60}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> d.pop('subbu':60)
SyntaxError: invalid syntax
>>> d.pop('subbu')
60
>>> d
{'srujana': 89, 'rishi': 76, 'veda': 70, 'sai': 100}
>>> del d['sai']
>>> d
{'srujana': 89, 'rishi': 76, 'veda': 70}
>>> d.setdefault('rishi',0)
76
>>> d.setdefault(sai',0)
...              
SyntaxError: unterminated string literal (detected at line 1)
>>> d.setdefault('sai',0)
...              
0
>>> d
...              
{'srujana': 89, 'rishi': 76, 'veda': 70, 'sai': 0}
