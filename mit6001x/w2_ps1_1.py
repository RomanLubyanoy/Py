s = 'azcbobobegghakl'
rez = 0
vowles = 'aeiou'
for vw in vowles:
    rez += s.lower().count(vw)
print 'Number of vowels: ' + str(rez)

'''
total = 0
for c in s:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        total += 1
print "Number of vowels: " + str(total)
'''