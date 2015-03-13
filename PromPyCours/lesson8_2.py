def find_fraction(summ):
    step = 1

    if summ == 0 or summ == 1 or summ == 2:
        return False
    if summ == 3:
        return 1, 2

    while True:
        for ch in range(summ / 2, 0, -1):
            zn = summ / 2 + step
            if ch + zn == summ and ch != zn:
                if not (ch % 2 == 0 and zn % 2 == 0) or (ch % 3 == 0 and zn % 3 == 0):
                    return ch, zn
        step += 1
#        if step > 10:
#            break


print find_fraction(62)
#print find_fraction(150000001)
#print find_fraction(15001)

# a = 150000001
#print (a / 2 ) % 2
