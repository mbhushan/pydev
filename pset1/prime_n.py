# author: mani bhushan
# problem set: 1 of Intro to computer science & programming.

import math

num = int(raw_input("Which prime number you are looking for? "))

count = 1

# initializing prime count to 1 - ie count starting from 2
prime_list = [2]

while len(prime_list) != num:
    count += 2
    pflag = 0
    r = int(math.sqrt(count))
    for p in prime_list:
        if p <= r:
            if count % p == 0:
                pflag = 1
                break
    if pflag == 0:
        prime_list.append(count)

print 'prime number {0} is: {1}'.format(num, prime_list[-1])
