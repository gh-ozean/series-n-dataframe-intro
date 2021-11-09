import numpy as np
import pandas as pd

''' NOTES
1. Pandas supports non-unique index values.
2. NaN (not a number) is the standard missing data marker used in pandas.
'''

def from_ndarray():
    print('1. From ndarray:')

    series_without_index = pd.Series(np.random.randn(7))
    print(f'Series without passing index:\n{series_without_index}')

    series_with_index = pd.Series(np.random.randn(7), index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    print(f'Series with passing index:\n{series_with_index}')

def from_dict():
    print('2. From dict:')
    s_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}

    series_without_index = pd.Series(s_dict)
    print(f'Series without passing index:\n{series_without_index}')

    series_with_index = pd.Series(s_dict, index=['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'])
    print(f'Series with passing index:\n{series_with_index}')

def from_scalar_value():
    print('3. From scalar value:')

    series_without_index = pd.Series(7)
    print(f'Series without passing index:\n{series_without_index}')

    series_with_index = pd.Series(7, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    print(f'Series with passing index:\n{series_with_index}')

def main():
    from_ndarray()
    from_dict()
    from_scalar_value()

if __name__ == '__main__':
    main()
