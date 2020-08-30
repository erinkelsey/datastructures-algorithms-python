import ctypes


class DynamicArray():
    '''Implementation of a Dynamic Array (Similar to Python list)
    '''

    def __init__(self):
        '''Initialize array

        Attributes:
            n (int): length of the array (default is 0)
            capacity (int): current capacity of array (default is 1)
            A (object): actual array in memory
        '''
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        '''Returns number of elements in array

        Returns:
            int: length of array
        '''
        return self.n

    def __getitem__(self, k):
        '''Get an array item at index k

        Args:
            k (int): index to retrieve item

        Returns:
            object: the item at index k

        Raises:
            IndexError: if the index k is out of bounds or invalid
        '''
        if not 0 <= k < self.n:
            raise IndexError('K is out of bounds :(')

        return self.A[k]

    def append(self, item):
        '''Append an item to the end of array, and adjust the length of array.

        If the capacity of the array has been reached, resize the array
        to 2x the current capacity, then add the item to the array.

        Args:
            item (int): the item to append to this array
        '''
        if self.n == self.capacity:
            self._resize(2*self.capacity)  # 2x, if capacity isn't enough

        self.A[self.n] = item
        self.n += 1

    def _resize(self, new_capacity):
        '''Resize internal array to capacity new_capacity.

        Args:
            new_capacity (int): the capacity to resize this array to
        '''
        B = self.make_array(new_capacity)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        '''Makes a new array with capacity new_capacity.

        Args:
            new_capacity (int): the capacity to make the array

        Returns:
            object: the newly created array with the specified capacity of 
            reserved bytes in memory
        '''
        return (new_capacity * ctypes.py_object)()

    def get_size(self):
        '''Gets the current size of array (in bytes)

        Returns:
            int: size of array in bytes
        '''
        return ctypes.sizeof(self.A)
