# Series
`Series` is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the `index`.

The passed `index` is a list of axis labels depending on what data is. [[implementation]](series_intro.py)

## Series is ndarray-like
`Series` acts very similarly to a `ndarray`, and is a valid argument to most `NumPy` functions. However, operations such as slicing will also slice the index.

## Series is dict-like
`Series` is like a fixed-size dict in that you can get and set values by index label.

## References
- [Series](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#series)
