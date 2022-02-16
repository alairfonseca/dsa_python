import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, index):
        if not 0 <= index < self._n:
            raise IndexError('invalid index')
        return self._A[index]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]

        self._A[k] = value
        self._n += 1

    def remove(self, value):
        for i in range(self._n):
            if self._A[i] == value:
                for j in range(i, self._n - 1):
                    self._A[j] = self._A[j + 1]

                self._A[self._n - 1] = None
                self._n -= 1

                return
        raise ValueError("value not found")

    def _resize(self, capacity):
        B = self._make_array(capacity)

        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = capacity

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()


if __name__ == "__main__":
    da = DynamicArray()

    for i in range(5):
        da.append(i)
        print("capacity", da._capacity)

    print("da[1]:", da[1])

    da.insert(2, da[2] * 2)
    print("da[2]:", da[2], "len:", da._n)

    da.remove(4)
    print("da[2]:", da[2], "len:", da._n)
