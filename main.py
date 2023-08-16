class A:
    def __init__(self, n):
        self._n = n +2

    def r(self):
        return self._n

if __name__ == "__main__":
    x = A(5)
    assert (x.r() == 7)
    x = A(2)
    assert (x.r() == 2)