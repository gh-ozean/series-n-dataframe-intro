import numpy as np
import pandas as pd

def is_ndarray_like():
    print('# Series is ndarray-like:')

    series = pd.Series(np.random.randn(7), index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    print(f'series =\n{series}')

    print('Slicing operations:')
    print(f'series[0] = {series[0]}')
    print(f'series[:3] =\n{series[:3]}')
    print(f'series.median() = {series.median()}')
    print(f'series[series > series.median()] =\n{series[series > series.median()]}')
    print(f'series[[0, 3, 4]] =\n{series[[0, 3, 4]]}')
    print(f'np.exp(series) =\n{np.exp(series)}')

    print('Series extension dtype:')
    print(f'series.dtype = {series.dtype}')

    print('Series extension array:')
    print(f'series.array =\n{series.array}')

    print('Series numpy ndarray:')
    print(f'series.to_numpy() =\n{series.to_numpy()}')

def main():
    is_ndarray_like()

if __name__ == '__main__':
    main()
