# Write a function, `count`
# that returns the units of time
# where each print statement is one unit of time
# and each evaluation of range also takes one unit of time

def count(n):
    # Your code here to count the units of time
    # it takes to execute clique
    t = 2 + n + (n*(n-1))/2
    return t

def clique(n):
    print "in a clique..."
    for j in range(n):
        for i in range(j):
            print i, "is friends with", j

def main():
	ans = count(4)
	print "ans: ", ans

if __name__ == '__main__':
	main()