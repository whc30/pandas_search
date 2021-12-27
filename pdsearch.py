

#TODO - change name and docs to make more general - this can apply for any object
def search(it,name,**kwargs):
    '''Search an iterable `it` for name `name`. This is commonly used to search the columns of Pandas DataFrames.
    Toggle case-sensitivity with `case` (default=False).
    Toggle removing underscores with `remove_us` (default=False).'''

    #Check input types
    it_names_orig = list(it)

    try:
        name = str(name)
    except:
        raise TypeError("Expected type for `name` input is str, got {}".format(type(name)))
    
    #Extra options through the kwargs
    case = kwargs.get('case') #Not case-sensitive by default
    if case == None:
        case = False
    rus = kwargs.get('remove_us')
    if rus == None:
        rus = False
        
    #Now the function
    if not case:
        it_names = [col.lower() for col in it_names_orig] #Make them lower case for easier checking
        name = name.lower() #Make the searched field lower case
    else:
        it_names = [col for col in it_names_orig]
    if rus:
        it_names = [col.replace('_','') for col in it_names]
    
    mapping = dict(zip(it_names,it_names_orig)) #A mapping for referring back to the original
    
    names = [mapping[col] for col in it_names if name in col]

    return names

if __name__ == '__main__':
    import pandas as pd

    df = pd.DataFrame({'A':[1,2,3],'b':[2,3,4],'ab3':[55,55,33]})
    print(search(df,'a'))

    listt = ['a','b','veg']
    print(search(listt,'v'))