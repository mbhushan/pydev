class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
    	cols = []
    	rows = []
    	for row in A:
    		for i in range(len(row)):
    			if row[i] == 0:
    				cols.append(i)
    				for j in range(len(row)):
    					row[j] = 0
    	print "A: ", A
    	print "cols: ", cols
    	for row in A:
    		for c in cols:
    			row[c] = 0
    	print "A Final: ", A
    

def main():
	data = [[1, 0],[1, 1],[1, 1]]
	data = [[0, 0], [1, 0]]
	sol = Solution()

	print "data: ", data
	sol.setZeroes(data)

if __name__ == '__main__':
	main()