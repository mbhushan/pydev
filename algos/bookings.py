class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def compare(self, a , b) :
        if a[0] <  b[0] :
            return -1
        elif a[0] == b [0] :
            if a[1] > b[1] :
                return -1
            elif a[1] == b[1] :
                return 0
            else :
                return 1
        else :
            return 1
            
    def hotel(self, arrive, depart, K):
        bookings = []
        for a in arrive:
            bookings.append((a, 0))
        for d in depart:
            bookings.append((d, 1))
        # sorted(bookings, key=lambda x:x[0])
        bookings.sort(cmp = self.compare)
        count = 0
        for i in range(len(bookings)):
            if bookings[i][1] == 0:
                count += 1
            elif bookings[i][1] == 1:
                count -=1
            if count > K:
                return 0
        return 1
