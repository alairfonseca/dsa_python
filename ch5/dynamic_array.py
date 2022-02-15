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

    def _resize(self, capacity):
        B = self._make_array(capacity)

        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = capacity

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()


if __name__ == "__main__":
    arr = DynamicArray()

    for i in range(5):
        arr.append(i)
        print("capacity", arr._capacity)

    print(arr[1])
