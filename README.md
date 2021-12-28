# PySearch

This is a simple package for searching a python iterable for key-words. It works on any object ```x``` for which ```list(x)``` is defined, including lists, dictionaries, sets, and pandas dataframes.

## Installation

The easiest way to install is by
```
pip install -e git+https://github.com/whc30/pysearch#egg=pysearch
```

## Search function 
```python
pysearch.search(it,name,**kwargs)
```
#### **Arguments**
- **it**: The python iterable that you wish to search. The only requirement is that ```list(it)``` is defined.
- **name**: The string name that you wish to search for.
- **kwargs**:
    - **case**: Boolean, whether you wish to do a case-sensitive search or not (default=False)
    - **remove_us**: Boolean, whether you wish to remove underscores (_) from the search (default=False)
    
#### **Returns**
Python list.

## Dependencies

No dependencies.

## Usage

This is best done with an example. It is done on a Pandas DataFrame as this is one of the more useful applications.
```python
import pandas as pd
from pysearch import search
```


```python
table1 = pd.DataFrame({'Apple':[1,2,3],'Banana':[7,6,8]})
table1
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Apple</th>
      <th>Banana</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>

```python
search(table1,'b')
```

```['Banana']```

**Note** that we can index the dataframe by this output:
```python
table1[search(table1,'b')]
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Banana</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>

More examples can be found in the examples .ipynb file.
