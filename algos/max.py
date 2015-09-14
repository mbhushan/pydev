#
# Write `max`
# 

def max(L):
    # return the maximum value in L
    ans = L[0]
    for i in range(1, len(L)):
    	if ans < L[i]:
    		ans = L[i]
    return ans

def test():
    L = [1, 2, 3, 4]
    assert 4 == max(L)
    L = [3, 6, 10, 9, 3]
    assert 10 == max(L)
    print "all tests successful!"

def main():
	test()

if __name__ == '__main__':
	main()