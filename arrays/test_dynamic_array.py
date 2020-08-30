from dynamic_array_implementation import DynamicArray
import pytest


def test_creation():
    arr = DynamicArray()
    assert len(arr) == 0


def test_append():
    arr = DynamicArray()
    arr.append(1)
    assert len(arr) == 1


def test_append_multiple():
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    assert len(arr) == 2


def test_get_index():
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    assert arr[0] == 1
    assert arr[1] == 2


def test_get_index_invalid_error():
    arr = DynamicArray()
    arr.append(1)
    with pytest.raises(IndexError) as err:
        arr[10]
    assert 'K is out of bounds :(' in str(err.value)


def test_string_array():
    arr = DynamicArray()
    arr.append('Hello, World!')
    assert arr[0] == 'Hello, World!'


def test_array_resize():
    arr = DynamicArray()
    assert arr.get_size() == 8
    arr.append(1)
    assert arr.get_size() == 8
    arr.append(2)
    assert arr.get_size() == 16
    arr.append(3)
    assert arr.get_size() == 32
    arr.append(4)
    assert arr.get_size() == 32
    arr.append(5)
    assert arr.get_size() == 64
