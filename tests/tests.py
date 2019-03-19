from pypackage import myFunction

def quick_sort():
    """
    make sure quick_sort works correctly
    """

    assert myFunction.quick_sort([8, 3, 2, 7, 4]) == [2, 3, 4, 7, 8], 'incorrect'
    assert myFunction.quick_sort([10, 1, 12, 9, 2]) == [1, 2, 9, 10, 12], 'incorrect'
    assert myFunction.quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], 'incorrect'

def merge_sort():
    """
    make sure merge_sort works correctly
    """

    assert myFunction.merge_sort([8, 3, 2, 7, 4]) == [2, 3, 4, 7, 8], 'incorrect'
    assert myFunction.merge_sort([10, 1, 12, 9, 2]) == [1, 2, 9, 10, 12], 'incorrect'
    assert myFunction.merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], 'incorrect'

def bubble_sort():
    """
    make sure bubble_sort works correctly
    """

    assert myFunction.bubble_sort([8, 3, 2, 7, 4]) == [2, 3, 4, 7, 8], 'incorrect'
    assert myFunction.bubble_sort([10, 1, 12, 9, 2]) == [1, 2, 9, 10, 12], 'incorrect'
    assert myFunction.bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], 'incorrect'

def fibonacci():
    """
    make sure fibonacci works correctly
    """

    assert myFunction.fibonacci(2) == 1, 'incorrect'
    assert myFunction.fibonacci(3) == 2, 'incorrect'
    assert myFunction.fibonacci(5) == 5, 'incorrect'

def factorial():
    """
    make sure factorial works correctly
    """

    assert myFunction.factorial(2) == 2, 'incorrect'
    assert myFunction.factorial(3) == 6, 'incorrect'
    assert myFunction.factorial(5) == 120, 'incorrect'

def sum_array():
    """
    make sure sum_array works correctly
    """

    assert myFunction.sum_array([1, 2, 5, 13]) == 21, 'incorrect'
    assert myFunction.sum_array([[1 ,4, 3], [4, 2, 8]]) == 22, 'incorrect'
    assert myFunction.sum_array(5) == 5, 'incorrect'

def reverse():
    """
    make sure reverse works correctly
    """

    assert myFunction.reverse('cows') == 'swoc', 'incorrect'
    assert myFunction.fibonacci('people') == 'elpoep', 'incorrect'
    assert myFunction.fibonacci('12345') == '54321', 'incorrect'
