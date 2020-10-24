"""
Summary: Class for creating list of prime factors for an integer
Date: 2020-10-24
Contributor(s):
    Mark Moretto

Example:
>>> p = Primes(64)
>>> p.prime_factors
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
"""



class Primes:
    """
    Class for creating list of prime factors for an integer


    >>> Primes(4).prime_factors
    [2, 3]

    >>> p = Primes(4)
    >>> p.prime_factors
    [2, 3]

    >>> Primes(4)
    <Primes 4 />

    >>> p = Primes("a")
    Traceback (most recent call last):
        ...
    TypeError: Integer data type expected.
    """
    def __init__(self, number):
        if isinstance(number, int):
            self.__n = number
            self.results = []
        else:
            raise TypeError("Integer data type expected.")

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.n} />"

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):
        if not isinstance(value, int):
            raise TypeError("Integer data type expected.")
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
        """Private method to find prime factors of an integer."""
        self.results = []
        self.p_list = [0] * self.n1

        for i in range(2, self.n1):
            if self.p_list[i] == 0:
                self.p_list[i] = i
                self.results.append(i)
            j = 0
            while True:
                if (j < len(self.results)
                        and self.results[j] <= self.p_list[i]
                        and (i * self.results[j]) <= self.n
                        ):

                    idx = i * self.results[j]
                    self.p_list[idx] = self.results[j]

                else:
                    break
                j += 1

    @property
    def prime_factors(self):
        """Call to calculate and return list of prime factors."""
        self.__efficient_prime_factors()
        return self.results



if __name__ == "__main__":
    import doctest
    doctest.testmod()
