# Pandas Search

This is a simple package for searching the columns of Pandas DataFrames for key-words.

## Search function 
```python
pdsearch.search(df,name,**kwargs)
```
#### **Arguments**
- **df**: The ```pandas.DataFrame``` that you wish to search.
- **name**: The string name that you wish to search for.
- **kwargs**:
    - **case**: Boolean, whether you wish to do a case-sensitive search or not (default=False)
    - **remove_us**: Boolean, whether you wish to remove underscores (_) from the search (default=False)
    
#### **Returns**
Python list.

## Dependencies

Depends only on Pandas, and should be version independent.

## Usage

This is best done with an example.
```python
import pandas as pd
from pdsearch import search
```


```python
table1 = pd.DataFrame({'Apple':[1,2,3],'Banana':[7,6,8]})
table1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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

```python
['Banana']
```

**Note** that we can index the dataframe by this output:
```python
table1[search(table1,'b')]
```
</style>
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