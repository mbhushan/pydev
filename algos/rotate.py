def rotateArray(a, b):
	ret = []
	if b >= len(a):
		m = b % len(a)
	else:
		m = b
	print "m, ", m
	for i in xrange(len(a)-m):
		ret.append(a[i + m])
	ret.extend(a[:m])
	return ret


def main():
	a = [1, 2, 3, 4, 5, 6]
	a = [ 14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35 ]
	b = 56
	ans = rotateArray(a, b)
	print "rotated array: ", ans

if __name__ == '__main__':
	main()
