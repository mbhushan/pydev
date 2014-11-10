# author: mani bhushan
# problem set: 1 of Intro to computer science & programming.

import math

num = int(raw_input("Which prime number you are looking for? "))


def getPrime(num):
    # initializing prime count to 1 - ie count starting from 2
    prime_list = [2]
    count = 1

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

    return prime_list

primes = getPrime(num)
sum = 0
for p in primes:
    sum += math.log(p)

print "{0} prime number is: {1}".format(num, primes[-1])
print "sum of log of all primes from 2 to {0} is: {1}".format(primes[-1], sum)
print "Ratio of {0} & {1} is: {2}".format(sum, primes[-1], (sum/primes[-1]))
