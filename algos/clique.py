#
# How many edges in a complete graph on n nodes? 
# 

def clique(n):
    # Return the number of edges
    # Try to use a mathematical formula...
    n = (n * (n-1)) / 2
    return n

def main():
	n = 10
	for i in range(3, 11):
		print "clique : ", i, " = ", clique(i)

if __name__ == '__main__':
	main()