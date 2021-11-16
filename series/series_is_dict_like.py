import numpy as np
import pandas as pd

def is_dict_like():
    print('# Series is dict-like:')

    series = pd.Series(np.random.randn(7), index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    print(f'series =\n{series}')

    print('Getting and setting values operations:')
    print(f'series["a"] = {series["a"]}')
    series["a"] = 7
    print(f'series =\n{series}')

    print(f'"d" in series = {"d" in series}')
    print(f'"h" in series = {"h" in series}')
    # print(f'series["h"] = {series["h"]}')     # KeyError: 'h'
    print(f'series["h"] = {series.get("h", np.nan)}')

def main():
    is_dict_like()

if __name__ == '__main__':
    main()
