import pandas as pd

def search(df,name,**kwargs):
    '''Search the columns of a Pandas dataframe `df` for columnname `name`.
    Toggle case-sensitivity with `case` (default=False).
    Toggle removing underscores with `remove_us` (default=False).'''

    #Check input types
    if not isinstance(df,pd.DataFrame):
        raise TypeError("Expected type for `df` input is a Pandas.DataFrame, got {}".format(type(df)))
    if type(name) == float or type(name) == int:
        name = str(name) #try, except?
    if type(name) != str:
        raise TypeError("Expected type for `name` input is str, got {}".format(type(name)))
    
    #Extra options through the kwargs
    case = kwargs.get('case') #Not case-sensitive by default
    if case == None:
        case = False
    rus = kwargs.get('remove_us')
    if rus == None:
        rus = False
        
    #Now the function
    df_cols_orig = list(df.columns)
    if not case:
        df_cols = [col.lower() for col in df.columns] #Make them lower case for easier checking
        name = name.lower() #Make the searched field lower case
    else:
        df_cols = [col for col in df.columns]
    if rus:
        df_cols = [col.replace('_','') for col in df_cols]
    
    mapping = dict(zip(df_cols,df_cols_orig)) #A mapping for referring back to the original
    
    cols = [mapping[col] for col in df_cols if name in col]

    return cols

if __name__ == '__main__':
    df = pd.DataFrame({'A':[1,2,3],'b':[2,3,4],'ab3':[55,55,33]})
    print(search(df,'a'))