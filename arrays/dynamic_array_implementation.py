import ctypes


class DynamicArray():
    """Implementation of a Dynamic Python Array
    """

    def __init__(self):
        """Initialize this Dynamic Array

          Attributes:
              n (int): length of the array
              capacity (int): current capacity of this array
              A (object): this array in memory
        """
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """Returns the length of this array

        Returns:
            int: length of this array
        """
        return self.n

    def __getitem__(self, k):
        """Get an array item at a specific index

        Args:
            k (int): index to retrieve item

        Returns:
            object: the item at index k

        Raises:
            IndexError: if the index k is out of bounds or invalid
        """
        if not 0 <= k < self.n:
            raise IndexError('K is out of bounds :(')

        return self.A[k]

    def append(self, item):
        """Append an item to the end of this array, and adjust the length of array.

        If the capacity of the array has been reached, resize the array
        to 2x the current capacity, then add the item to the array.

        Args:
            item (int): the item to append to this array
        """
        if self.n == self.capacity:
            self._resize(2*self.capacity)  # 2x, if capacity isn't enough

        self.A[self.n] = item
        self.n += 1

    def _resize(self, new_capacity):
        """Resize the current array to a specific capacity.

        Args:
            new_capacity (int): the capacity to resize this array to
        """
        B = self.make_array(new_capacity)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        """Make an array with a specific capacity.

        Args:
            new_capacity (int): the capacity to make the array

        Returns:
            object: the newly created array with the specified capacity of 
            reserved bytes in memory
        """
        return (new_capacity * ctypes.py_object)()

    def get_size(self):
        """Gets the current size of array (in bytes)

        Returns:
            int: size of array in bytest
        """
        return ctypes.sizeof(self.A)
