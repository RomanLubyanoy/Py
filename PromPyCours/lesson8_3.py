# -*- coding:utf-8 -*-
"""
Розробити функцію bouquets(narcissus_price, tulip_price, rose_price, summ),
яка приймає 4 аргументи -- додатні дійсні числа (ціни за один нарцис,
тюльпан та троянду, і суму грошей у кишені головного героя),
та повертає ціле число -- кількість варіантів букетів, які можна скласти
з цих видів квітів, таких щоб вартість кожного букету не перевищувала summ.

Не забути, що букети з парною (загальною) кількістю квітів живим дівчатам
не дарують. Тести із некоректними даними не проводяться.

Приклад послідовності дій для тестування:
print bouquets(1,1,1,5) # 34
print bouquets(2,3,4,10) # 12
print bouquets(2,3,4,100) # 4019
print bouquets(200,300,400,10000) # 4019
print bouquets(200,300,400,100000) # 3524556
"""


def bouquets(narcissus_price, tulip_price, rose_price, summ):
        rez = 0
        for na in range(int(summ // narcissus_price + 1)):
            for tu in range(int(summ // tulip_price + 1)):
                if (na + tu) % 2 == 0 and na*narcissus_price + tu*tulip_price == summ:
                        break
                if na*narcissus_price + tu*tulip_price > summ:
                        break
                for ro in range(int(summ // rose_price + 1)):
                    if (na + tu + ro) % 2 == 0:
                        continue
                    if na*narcissus_price + tu*tulip_price > summ:
                        break
                    if na*narcissus_price + ro*rose_price > summ:
                        break
                    if tu*tulip_price + ro*rose_price > summ:
                        break
                    if na*narcissus_price + tu*tulip_price + ro*rose_price > summ:
                        break
                    if na*narcissus_price + tu*tulip_price + ro*rose_price <= summ:
                        rez += 1
        return rez
#                    print na, tu, ro, '-', na*narcissus_price + tu*tulip_price + ro*rose_price

print bouquets(21.25,13.6,10.5,100) #51
print bouquets(15.5,4.1,5.99,21.75)
#print bouquets(1,1,1,5) # 34
#print bouquets(2,3,4,10) # 12
print bouquets(2,3,4,100) # 4019 (11605)(8037)
#print bouquets(200,300,400,100000) #3524556 (7049112)
#print (1) % 2
#print 'TestIsDone success 2 and done'


#print bouquets(22, 44 , 150,20000) # 4666877


#print ['{0:06}'.format(i) for i in xrange(1000000) if sum(map(int,str(i))) == 20]