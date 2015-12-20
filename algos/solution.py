class Solution(object):
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
    	res = []
    	tmp = []
    	print "A: ", A
    	for i in range(len(A)):
    		print A[i],
    	for i in range(len(A)):
    		print "inside loop"
    		if A[i] >= 0:
    			tmp.append(A[i])
    			print "tmp: ", tmp
    		if A[i] < 0:
				if sum(tmp) > sum(res):
					res = tmp[:]
					print "res1: ", res
				elif sum(tmp) == sum(res):
					if len(tmp) > len(res):
						res = tmp[:]
				tmp = []
			# print "looping: "
		print "res: ", res
		return res


def main():
	A = [1, 2, 5, -7, 2, 5]
	sol = Solution()
	ans = sol.maxset(A)
	# print "solution: ", sol.maxset(A)

if __name__ == '__main__':
	main()