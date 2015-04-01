#!/usr/bin/env python

# num = raw_input('Please think of a number between 0 and 100!')
num = 12
low = 0
hi = 100
check = hi / 2

while True:
    print 'Is your secret number ' + str(check) + '?'
    while True:
        task = raw_input(
            "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        if (task == 'h' or
                    task == 'l' or
                    task == 'c'):
            break
        else:
            print 'Sorry, I did not understand your input.'

    if task == 'h':
        hi = check
        check = (hi + low) / 2
    elif task == 'l':
        low = check
        check = (hi + low) / 2
    elif task == 'c':
        print 'Game over. Your secret number was: ' + str(check)
        break
"""
cn = 0
while check != num:
	if check > num:
		hi = check
		check = (hi + low) / 2
	else:
		low = check
		check = (hi + low) / 2
	if cn == 20:
		break
	cn += 1
	print check
"""
