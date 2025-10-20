import numpy as np

def array_basics():
    nums = [1, 2, 3, 4, 5]
    arr = np.array(nums)
    print('Original list: ', nums)
    print('NumPy array: ', arr)
    print('Array type: ', type(arr))
    print('Shape: ', arr.shape)
    print('Data type: ', arr.dtype)


def array_operations():
    arr = np.array([10, 20, 30 , 40, 50])
    print('\nArray: ', arr)
    print('Sum: ', np.sum(arr))
    print('Mean: ', np.mean(arr))
    print('Squared: ', arr ** 2)
    print('Add 5 to all elements: ', arr + 5)


def test_array_operations():
    arr = np.array([1, 2, 3])
    assert np.sum(arr) == 6
    print('NumPy test passed!')


if __name__ == '__main__':
    array_basics()
    array_operations()
    test_array_operations()