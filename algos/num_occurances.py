

def read_input():
    data = raw_input("Enter numbers separated by space: ")
    data = data.strip().split(' ')
    nums = [int(n.strip()) for n in data]
    return sorted(nums)


def num_occurances(nums, low, high, key):
    if low > high:
        return 0
    mid = low + (high-low)/2
    if nums[mid] < key:
        return num_occurances(nums, mid+1, high, key)
    if nums[mid] > key:
        return num_occurances(nums, low, mid-1, key)
    return num_occurances(nums, low, mid-1, key) + 1 + \
        num_occurances(nums, mid+1, high, key)


def main():
    data = read_input()
    print "data: ", data
    key = raw_input("Enter search key: ").strip()
    key = int(key)
    n = len(data)
    result = num_occurances(data, 0, n-1, key)
    print "number of occurances of %d: %d" % (key, result)

if __name__ == '__main__':
    main()
