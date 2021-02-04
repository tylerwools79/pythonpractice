#The below function checks every nth value in the list of purchases to see if it is divisible by d. Yields the first of such values in the list
class Prizes(object):
    def __init__(self,purchases,n,d):
        self.purchases=purchases
        self.n=n
        self.d=d
    def __iter__(self):
        for i,x in enumerate(self.purchases):
            if(i+1) % self.n == 0 and x % self.d == 0:
                yield i+1


def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))
