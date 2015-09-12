# Write a program that returns the number of edges
# in a star network that has `n` nodes 
#

def star_network(n):
    # return number of edges
    return n-1

def main():
	n = 10
	edges = star_network(n)
	print "%d: %d" % (n, edges)

if __name__ == '__main__':
	main()