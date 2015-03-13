"""
# M2
def convert_n_to_m(x, n, m):
    list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if x < 0 :
        return False
    if m == 1:
        return '0' * int(str(x), n)
    try:
        num = int(str(x), n)
        if num == 0:
            return 0
        rez = ''
        while num:
            rez = list[num % m] + rez
            num //= m
            if len(rez) > 50:
                dump = [x, n, m]
                return dump
    except ValueError:
        return False
    return rez

#print convert_n_to_m([123], 4, 3)
#print convert_n_to_m("0123", 5, 6)
#print convert_n_to_m("123", 3, 5)
#print convert_n_to_m(4, 10, 2)
print convert_n_to_m(123123123123123123123, 10, 10)


# 6.4
def find_most_frequent(text):
    punct = ',.:;!?- '
    word = ''
    list_of_words = []
    rez = ['']
    count = 0

    if not text:
        return []

    if text[-1] not in punct:
        text += '.'

    for i in text:
        if i not in punct:
            word += i
        else:
            if word:
                list_of_words.append(word.lower())
            word = ''

    for items in list_of_words:
        if list_of_words.count(items) > count:
            count = list_of_words.count(items)
            rez[0] = items
    for items in list_of_words:
        if list_of_words.count(items) == count:
            if items not in rez:
                rez.append(items)

    print(sorted(rez))
    return text


find_most_frequent('a a aa a b b b b b a a')
find_most_frequent('This is the front page of the Simple English Wikipedia. Wikipedias are places where people work together to write encyclopedias in different languages. We use Simple English words and grammar here. The Simple English Wikipedia is for everyone! That includes children and adults who are learning English. There are 120,571 articles on the Simple English Wikipedia. All of the pages are free to use. They have all been published under both the Creative Commons Attribution/Share-Alike License 3.0 and GNU Free Documentation License. You can help here! You may change these pages and make new pages. Read help pages and other good pages to learn how to write pages here. If you need help, you may ask questions at Simple talk.')
find_most_frequent("Load up on guns; bring your friends It's fun to lose and to pretend She's over-bored and self-assured Oh no, I know a dirty word Hello,hello,hello,how low Hello,hello,hello,howlow Hello,hello,hello,how low Hello,hello,hello")
find_most_frequent("And I forget just why I taste; Oh yeah, I guess it makes me smile; I found it hard; it's hard to find; Oh well, whatever, never mind")

# 6.3
def saddle_point(matrix):
    row = len(matrix)
    col = len(matrix[0])
    rez = []

    if row == col == 1:
        rez = [0, 0]
        return tuple(rez)

    for i in range(row):
        for j in range(col):
#            print('--')
#            print (matrix[i][j])
#            print('--')
            c_list = []
            r_list = []
            for c_item in range(col):
                if c_item != j:
                    c_list.append(matrix[i][c_item])
#                    if matrix[i][c_item] > matrix[i][j]:
#                        c_flag = True
#                        rez.append(j)
#                    print(matrix[i][c_item])

            for r_item in range(row):
                if r_item != i:
                    r_list.append(matrix[r_item][j])
#                    if matrix[r_item][j] < matrix[i][j]:
#                        r_flag = True
#                        rez.append(i)
#                    print(matrix[r_item][j])
#            print(c_list)
#            print(r_list)
            if min(c_list) > matrix[i][j] > max(r_list):
                rez.append(i)
                rez.append(j)


#    if c_flag and r_flag:
#        rez.append(i)
#        rez.append(j)
    if not rez:
        print False
        return False
    print(tuple(rez))

    return tuple(rez)


saddle_point([[1, 2, 3], [3, 2, 1]])
saddle_point([[1, 2, 3], [0, 2, 1]])
saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]])
saddle_point([[21]])

# 6.2
def encode_morze(text):
    morse_code = {
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--.."
    }
    code_list = []
    rez_list = []
    rez = ''

    for i in text:
        # print(type(i))
        if type(i) is str:
            if i.upper() in morse_code:
                code_list.append(morse_code[i.upper()])
            if i == ' ':
                code_list.append('T')
    for items in code_list:
        rez_list.append('__')
        for symbol in items:
            if symbol == '.':
                rez_list.append('^')
                rez_list.append('_')
            if symbol == '-':
                rez_list.append('^^^')
                rez_list.append('_')
            if symbol == 'T':
                rez_list.append('__')
            # print symbol



    rez = ''.join(rez_list)
    print(rez[2:-1])
    return rez[2:-1]

encode_morze('Morze code')
encode_morze('Prometheus')
encode_morze('SOS')
encode_morze('Sd s s!')

# 6.1
def count_holes(n):
    rez = 0
    dic = {'0':1, '1':0, '2':0, '3':0, '4':1, '5':0, '6':1, '7':0, '8':2, '9':1}
#    print(type(n))
    if type(n) is str or type(n) is int or type(n) is long:
#	print(type(n))
	if type(n) is long:
	    t = abs(long(n))
	else:
    	    if str(n).isdigit():
		t = abs(long(n))
	    else:
		print('ERROR')
		return 'ERROR'
#	print(type(t))
	for i in str(t):
	    rez += dic[i]
	print(rez)
	return rez    
    else:
	print('ERROR')
	return 'ERROR'
	
#    print(rez)
#    return rez

#count_holes('888888888888888888888.0')    
count_holes(-888888888888888888888)
count_holes('sdad')
count_holes(906)
count_holes(-8.0)

#5.4 !!!!!!!!!!!!!!! ERROR
def file_search(folder, filename):
    res_list = []
    res_str = ''
    if isinstance(folder, list):
	for item in folder:
    	    res_str = res_str + file_search(item, filename)
	return res_str
    else:
	if folder == filename:
	    return folder + 'GO'
#	file_search(folder[0], filename)
#        res_list.append(folder[0])
        return folder
    
#    for j in res_list:
#        res_str = j + '/' + filename
#    return res_str
#	print(i)	
#    return str(folder[0])
#def p_search(p, f):

#    for i in p:
#	if i == f:
#	    return p[0]
#	else:
#	    return false

#file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
#print(file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt'))
r = []
l = [ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py']
f = 'hereiam.py'
r.append(file_search(l, f))
print(l)
#for i, v in enumerate(l):
#    print(i, v)
print(r)

# 5.3
def super_fib(n, m):
    l = [1 for x in range(m)]
    
    for i in range(n):
	l.append(sum(l[i:i+n]))
    
    return l[n-1]
    
print(super_fib(8,2))
print(super_fib(9,3))

fib_pre = 1
fib_pre_pre = 0
fib = 1
for i in range(9):
    fib = fib_pre + fib_pre_pre
    fib_pre_pre = fib_pre
    fib_pre = fib
    print(fib)

#5.2
def counter(a, b):
    in_a = str(a)
    in_b = str(b)
    match = 0
    in_b = del_dup(in_b)
    
    for i in range(len(in_b)):
	if in_a.count(in_b[i]) > 0:
	    match += 1
    
    return match

def del_dup(s):
    s1 = ''
    for i in (set(s)):
	s1 += i
    return s1   

print(counter(12345, 567))
print(counter(1233211, 12128))
print(counter(123, 45))

#5.1
def clean_list(input_list):
    
    if len(input_list) !=0:
        output_list = [input_list[0]]
    else:
	return []
    for i in range(1,len(input_list)):
	c = 0
	for j in range(len(output_list)):
	    if input_list[i] == output_list[j] and type(input_list[i]) == type(output_list[j]):
		c += 1
		break
	if c == 0:
		output_list.append(input_list[i])

    return output_list
    
print(clean_list([1, 1.0, '1', -1, 1]))
print(clean_list(['qwe', 'reg', 'qwe', 'REG']))
print(clean_list([32, 32.1, 32.0, -123]))
print(clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]))
print(clean_list([]))

#M1
import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = ""
s = str(sys.argv[1]).replace(" ", "")
l = []

for i in range(len(s)/5):
    l.append(s[i*5:i*5 + 5])

for i in range(len(l)):
    word = list(l[i])
    for j in range(len(word)):
	if word[j].islower():
	    word[j] = "a"
	else:
	    word[j] = "b"
    l[i] = ''.join(word)
    
for i in l:
    result = result + alphabet[key.find(str(i))]
print(result)

#4.4
import sys

range_start = sys.argv[1]
range_end = sys.argv[2]
rez = 0

#if range_start == range

for a in range(int(range_start), int(range_end)+1):
	l = []
	c = 0
	for i in range(6):
	    if i < 6 - len(str(a)):
		l.append(0)
            else:
			l.append(int(str(a)[c]))
			c += 1
	print(l)
	if (l[3] + l[4] + l[5]) == l[0] + l[1] + l[2]:
	    rez += 1

print(rez)

#4.3
import sys

s = sys.argv[1]
l = 0

for i in s:
    if i == "(": 
	l +=1
	if l < 0: 
	    break
    elif i == ")":
	l -=1
	if l < 0: 
	    break
if l == 0:
    print("YES")
else:
    print("NO")

#4.2
import sys

s = sys.argv[1:]
rez = ""
for word in s[::-1]:
    rez = rez + word + " "

#rez.replace('[',''))

#print(rez[::-1].lstrip())
print(rez)

#4.1
import sys

s = str(sys.argv[1]).replace(' ', '').lower()

if s[:len(s)] == s[::-1]:
    print("YES")
else:
    print("NO")

print(s[:len(s)])
print(s[::-1])

#print(len(s)/2-1)
#print(s[:len(s)/2-1:-1])
#print(s[:len(s)/2])
#print(s[2:range(len(s))/2])
#for i in range(len(s)/2):
#    print(s[i])
#    print(s[-i])

#3.2
import sys

n = int(sys.argv[1])
fib1 = 0
fib2 = 1
fib_sum = 0

if n < 0:
    print('Wrong input')
else:
    if n == 0 :
	print(fib1)
    else:
	if n == 1:
	    print(fib2)
	else:
	    for counter in range(n-1):
		fib_sum = fib1 + fib2
		fib1 = fib2
		fib2 = fib_sum
	    print fib_sum

#3.1
a = float(raw_input('Enter a: '))
b = float(raw_input('Enter b: '))
c = float(raw_input('Enter c: '))

import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a >= b + c or b >= a + c or c >= a + b:
    print('not triangle')
else:
    print('triangle')
"""