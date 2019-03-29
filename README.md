# whyme

whyme is a Python library for sorting with a handful of recursive functions as well.

## Installation

To install whyme:

```bash
pip install git+https://github.com/sh3zaad/whyme.git
```

## Usage

```python
import whyme

whyme.sum_array([1,0,4,2]) # returns 7
whyme.fibonacci(2) # returns 1
whyme.factorial(5) # returns 120
whyme.reverse('word') # returns 'drow'
whyme.bubble_sort([9,4,6,12,2]) # returns [2, 4, 6, 9, 12]
whyme.merge_sort([9,4,6,12,2]) # returns [2, 4, 6, 9, 12]
whyme.quick_sort([9,4,6,12,2]) # returns [2, 4, 6, 9, 12]
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
