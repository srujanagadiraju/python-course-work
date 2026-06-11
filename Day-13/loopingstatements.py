#str list tuple set dict range()
'''
for var in seq:
    print(var)
'''
'''
s='srujana gadiraju'
for name in s:
    print(name)
'''
'''
l=['sugar','salt','oil']
for item in l:
    print(item)
'''
'''
t= ('1.intro','2.basics','3.final')
for i in t:
    print(i)
'''
'''
s={'laptop','mouse','keyboard','phone'}
for i in s:
    print(i)
'''
'''
d={'name':'srujana','batch':'55','course':'PFS','skills':['python','mysql','java']}
for i in d:
    print(i,d[i])
'''

#range functions
#range(start,stop+1,step) => (0,n,+1)
'''
for i in range(1,11):
    print(i)
'''
'''
for i in range(2,51,2):
    print(i)
'''
'''
for i in range(5,101,5):
    print(i)
'''
'''
for i in range(20,0,-1):
    print(i)
'''
'''
for i in range(6):
    print(i)
'''
#iterate using index(str list tuple)
#range-str list tuple
'''
s='srujana'
for i in range(len(s)):
    print(i,s[i])
'''
'''
l=[1,2,3,4,5,6]
for i in range(len(l)):
    print(i,l[i])
'''
'''
t=(2,3,4,5,6)
for i in range(len(t)):
    print(i,[t])
'''
#enumerate-str list tuple set
'''
s='srujana'
for i in enumerate(s):
    print(i[0],i[1])
'''
'''
l=[1,2,3,4,5,6]
for i in enumerate(l):
    print(i[0],i[1])
'''
'''
t=(1,3,4,5,6)
for i in enumerate(t):
    print(i[0],i[1])
'''
'''
s={9,8,7,6,5}
for i in enumerate(s):
    print(i[0],i[1])
'''
#break
'''
for i in range(10):
    if i==5:
        break
    print(i)
'''
#continue
'''
for i in range(10):
    if i==5:
        continue
    print(i)
'''
#pass
'''
for i in range(10):
    pass
'''
#example
'''
s='srujana'
for i in s:
    if i in 'aeiouAEIOU':
        print(i)
'''
#example
'''
l=[12,2,3,34,45,5,6,67,68,2,3,4,5]
for i in l:
    if i%2==0:
        print(i)
'''
#example
'''
d={'laptops':0,'chargers':2,'phone':3,'tab':8}
for i in d:
    if d[i]:
        print(i)
'''
#example
'''
t=(9,12,3,4,6,8)
for i in range(len(t)):
    print(i*t[i])
'''
#example
names = {'srujana','rishi','veda'}
for i in names:
    print(i.upper())





















