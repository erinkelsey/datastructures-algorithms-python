# Arrays

- Arrays denote the representation of a group of related variables, stored one after another in a contiguous portion of the computer's memory
- Each cell of an array uses the same number of bytes
- Cell can be accessed in constant time, or O(1), and the memory address can be computed using the calculation: _start + (cellsize)(index)_

### Referential Arrays

- Each element is a _reference_ to an object
- A single list instance may include multiple references to the same object, as separate elements of the list
- A single object can be an element of two or more lists
- When computing a slice of a list, the result is a new list instance, and the new list has references to the same elements that were in the original list

### Dynamic Arrays

- Provide a means to grow the array _A_ that stores a number of elements
- We can't actually grow array _A_, as it's capacity is fixed
- If an element is appended to a list at a time when the underlying array is full, add the new element by using following algorithm

#### Algorithm:

1. Allocate a new array _B_ with larger capacity

2. Set _B[i] = A[i]_, for _i = 0, ..., n-1_, where _n_ denotes current number of items

3. Set _A = B_, that is, we henceforth use _B_ as the array supporting the list

4. Insert the new element in the new array

#### How large is the new array _B_ that is created?

The commonly used rule is for the new array to have twice the capacity of the existing array.
