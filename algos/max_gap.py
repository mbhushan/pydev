def maximumGap(A):
	aux = []
	n = len(A)

	for i in range(n):
		aux.append((A[i], i))

	sorted(aux, key=lambda x:x[0])

	maxgap = -1
	index = aux[n-1][1]
	gap = 0

	for i in range(n-1, 0, -1):
		if aux[i][1] < index:
			gap = index - aux[i][1]
		elif aux[i][1] > index:
			index = aux[i][1]
		if gap > maxgap:
			maxgap = gap

	return maxgap



def main():
	# A = [4, 3, 5, 2, 1, 3, 2, 3]
	A = [3, 5, 4, 2]
	res = maximumGap(A)
	print "res: ", res


if __name__ == '__main__':
	main()

