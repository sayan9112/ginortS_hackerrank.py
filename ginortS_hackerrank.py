#1
print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')
 
#2
print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

#3
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

#4
import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')



#https://www.hackerrank.com/challenges/ginorts/problem