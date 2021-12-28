from setuptools import setup

VERSION = '0.1.0' 
DESCRIPTION = 'Search function for python iterable'

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

# Setting up
setup(
        name="pysearch", 
        version=VERSION,
        author="William Henry Clare",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        url="https://github.com/whc30/pysearch",
        install_requires=[],
        
        keywords=['python'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ]
)