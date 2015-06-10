'''
Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
'''

s = 'azcbobobegghakl'
#s = 'abcbcd'
#s = 'abcdefghijklmnopqrstuvwxyz'
#s = 'nzvtjcqipjpbiuiashujfmmp'
import string

alpha = string.ascii_lowercase

sub = []
rez = []
pos = 1
pre = ''
for i in s:
    if len(sub) > len(rez):
        rez = sub
    sub = [i]
    pre = i
    for j in s[pos:]:
        if alpha.find(j) >= alpha.find(pre):
            sub.append(j)
            pre = j
        else:
            pos += 1
            break

print 'Longest substring in alphabetical order is: ', ''.join(rez)

'''
curString = s[0]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= curString[-1]:
        curString += s[i]
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest
'''