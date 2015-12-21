def diagonal(A):
	res = []
	for i in range(2 * (len(A) - 1)) :
		if i < len(A) :
			z = 0
		else :
			z = i - len(A) + 1
			temp = []
			for j in range(z, i - z + 1) :
				temp.append(A[j] [i - j])
				res.append(temp)
	return res

def printDiagonal(A):
	res = []
	for i in range((2*(len(A)-1))+1):
		tmp = []
		for j in range(i+1):
			if (j<len(A)) and ((i-j) < len(A)):
				tmp.append(A[j][i-j])
				# print "res_1", res[-1]
				
				if len(res) == 0:
					res.append(tmp)
				elif tmp != res[-1]:
					res.append(tmp)
	return res



def main():
	A = [[1,2,3],[4,5,6],[7,8,9]]
	# A = [[8, 6, 8], [8, 1, 0], [8, 6, 8]]
	res = printDiagonal(A);
	print res

if __name__ == '__main__':
	main();