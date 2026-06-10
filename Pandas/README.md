 # Data Analysis

This project uses the Python `pandas` library to load, clean, and analyze car sales data.


## ʕ·ᴥ·ʔ 

- `pandas` is a Python library for data manipulation and analysis.
- It provides `DataFrame` and `Series` objects for working with structured tabular data.
- Common tasks include loading CSV files, filtering rows and columns, grouping and aggregating data, and handling missing values.

## Example

```python
import pandas as pd

df = pd.read_csv("car-sales.csv")
print(df.head())
print("Average price:", df["price"].mean())
```

## Data files

- `car-sales.csv` — original car sales dataset
- `Exported-car-sales.csv` — exported or processed dataset

