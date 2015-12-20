def maxset(A):
	res = []
	tmp = []
	for i in range(len(A)):
		if A[i] >= 0:
			tmp.append(A[i])
		else:
			if sum(tmp) > sum(res):
				res = tmp[:]
			elif sum(tmp) == sum(res):
				if len(tmp) > len(res):
					res = tmp[:]
			tmp = []
	# print "result: ", res
	return res



def main():
	A = [1, 2, 5, -7, 2, 5]
	res = maxset(A)
	print "result: ", res


if __name__ == '__main__':
	main()