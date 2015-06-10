'''
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
'''

s = 'azcbobobegghakl'
rez = 0
for c in range(len(s) - 2):
    rez += s[c:c+3].count('bob')
print 'Number of times bob occurs is:', rez
'''
numBobs = 0
for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        numBobs += 1
print 'Number of times bob occurs is:', numBobs
'''
