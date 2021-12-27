from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Search for Pandas dataframe columns'
LONG_DESCRIPTION = 'Search Pandas dataframe columns for a specified name'

# Setting up
setup(
        name="pandas_search", 
        version=VERSION,
        author="Will Clare",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['pandas'],
        
        keywords=['python', 'pandas'],
        classifiers= [
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)