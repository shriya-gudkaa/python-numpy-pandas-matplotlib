# 🐍 Python — NumPy · Pandas · Matplotlib
 
A hands-on learning repository covering the three core Python libraries used in **Data Science and Machine Learning** — built as part of my ML learning journey.
 
---
 
## 📌 About
 
This repo contains beginner-to-intermediate level Python scripts organized by library. Each file focuses on one concept, includes comments explaining what and why, and uses small practical examples to make things easy to follow.
 
It covers the foundational toolkit every ML engineer works with before diving into model building.
 
---
 
## 📁 Repository Structure
 
```
python-numpy-pandas-matplotlib/
│
├── numpy/
│   ├── array_creation.py
│   ├── array_operations.py
│   ├── broadcasting.py
│   ├── concatenation_and_splitting.py
│   ├── indexing_and_slicing.py
│   ├── statistical_functions.py
│   ├── rounding_functions.py
│   ├── ufuncs_and_math_functions.py
│   └── file_handling.py
│
├── pandas/
│   ├── series_creation.py
│   ├── series_attributes_and_operations.py
│   ├── dataframe_creation.py
│   ├── dataframe_attributes_and_inspection.py
│   ├── dataframe_selection_and_indexing.py
│   ├── Modifying_dataframe.py
│   ├── handling_missing_data.py
│   ├── sorting_and_aggregation.py
│   ├── time_series_operations.py
│   ├── csv_operations.py
│   └── albums.csv / random_stock_market_dataset.csv
│
└── matplotlib/
    ├── plot.py
    ├── bar.py
    ├── pie.py
    ├── hist.py
    ├── scatter_plot.py
    ├── boxplot.py
    └── subplot.py
```
 
---
 
## 📚 What's Covered
 
### 🔢 NumPy
| File | Concepts |
|------|----------|
| `array_creation.py` | `np.array()`, `zeros()`, `ones()`, `arange()`, `linspace()`, `eye()`, `full()`, `random` |
| `array_operations.py` | Arithmetic, reshape, transpose, dot product |
| `broadcasting.py` | Broadcasting rules across different shaped arrays |
| `indexing_and_slicing.py` | 1D/2D indexing, boolean masking, fancy indexing |
| `concatenation_and_splitting.py` | `concatenate()`, `stack()`, `split()`, `hsplit()`, `vsplit()` |
| `statistical_functions.py` | `mean()`, `median()`, `std()`, `var()`, `argmax()`, `cumsum()` |
| `rounding_functions.py` | `floor()`, `ceil()`, `round()`, `trunc()` |
| `ufuncs_and_math_functions.py` | Universal functions — `sin()`, `exp()`, `log()`, `sqrt()` |
| `file_handling.py` | `save()`, `load()`, `savetxt()`, `loadtxt()` |
 
### 🐼 Pandas
| File | Concepts |
|------|----------|
| `series_creation.py` | Creating Series from lists, dicts, scalars |
| `series_attributes_and_operations.py` | Index, values, dtype, arithmetic ops |
| `dataframe_creation.py` | DataFrame from dict, list, NumPy array, Series |
| `dataframe_attributes_and_inspection.py` | `shape`, `info()`, `describe()`, `dtypes`, `head()` |
| `dataframe_selection_and_indexing.py` | `loc[]`, `iloc[]`, column selection, conditional filtering |
| `Modifying_dataframe.py` | Adding/renaming/dropping columns, updating values |
| `handling_missing_data.py` | `isnull()`, `dropna()`, `fillna()`, `duplicated()` |
| `sorting_and_aggregation.py` | `sort_values()`, `groupby()`, `agg()` |
| `time_series_operations.py` | `to_datetime()`, resampling, date indexing |
| `csv_operations.py` | `read_csv()`, `to_csv()` with real datasets |
 
### 📊 Matplotlib
| File | Concepts |
|------|----------|
| `plot.py` | Line plot — `plt.plot()`, labels, grid |
| `bar.py` | Bar chart — vertical/horizontal bars |
| `pie.py` | Pie chart — labels, explode, percentage |
| `hist.py` | Histogram — bins, frequency distribution |
| `scatter_plot.py` | Scatter plot — correlation visualization |
| `boxplot.py` | Box plot — spread, outliers, quartiles |
| `subplot.py` | Multiple plots in one figure using `plt.subplot()` |
 
---
 
## 🛠️ Requirements
 
```bash
pip install numpy pandas matplotlib
```
 
Python 3.x recommended.
 
---
 
## ▶️ How to Run
 
Clone the repo and run any file directly:
 
```bash
git clone https://github.com/shriya-gudkaa/python-numpy-pandas-matplotlib.git
cd python-numpy-pandas-matplotlib
 
# Example
python numpy/array_creation.py
python pandas/handling_missing_data.py
python matplotlib/subplot.py
```
 
---
 
## 🎯 Purpose
 
This repo was built purely for **learning and practice** — to get comfortable with the tools that power every ML/Data Science workflow before moving on to model building with Scikit-learn.
 
---
 
## 👩‍💻 Author
 
**Shriya Gudka**  
[![GitHub](https://img.shields.io/badge/GitHub-shriya--gudkaa-181717?style=flat&logo=github)](https://github.com/shriya-gudkaa)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Shriya%20Gudka-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/shriya-gudka)
 
