

class Primes:
    def __init__(self, n):
        self.__n = n
        self.set(n)


    def set(self, value):
        self.p_list = [0] * self.n1
        self.results = []

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):
        if not isinstance(value, int):
            print("Expected integer data type!")
        else:
            self.__n = value

    @property
    def n1(self):
        return self.n + 1

    @property
    def nn(self):
        return self.n ** 2

    @property
    def nnn(self):
        return self.n ** 3

    def __efficient_prime_factors(self):
        self.results = []
        for i in range(2, self.n1):
            if self.p_list[i] == 0:
                self.p_list[i] = i
                self.results.append(i)
            j = 0
            while True:
                if j < len(self.results) and self.results[j] <= self.p_list[i] and (i * self.results[j]) <= self.n:
                    idx = i * self.results[j]
                    self.p_list[idx] = self.results[j]
                else:
                    break
                j += 1

    @property
    def prime_factors(self):
        self.__efficient_prime_factors()
        return self.results



def tests():
    """Sample tests for instantiation of class and run of prime_factors."""
    
    p4 = Primes(4)
    assert (p4.prime_factors == [2, 3]), "Primes(4) error"
    
    
    p64 = Primes(64)
    assert (p64.prime_factors == \
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]), \
            "Primes(64) error"


if __name__ == "__main__":
    # Run tests.
    tests()
