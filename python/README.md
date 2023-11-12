# Python Implementation (PyPI Package)

Status: **WIP** (cf. TODO.md)

# Scrapbook for PyPI (Testing)
+ Find here on PyPI: https://test.pypi.org/project/mopp/
+ Installing the package `pip install -i https://test.pypi.org/simple/ mopp==1.0.1`

# Scrapbook local building
+ Install the requirements
+ Local build using: python3 -m build  
+ pip3 install dist/mopp-1.0.1.tar.gz 
+ python3 -m twine upload --repository testpypi dist/mopp-1.0.1.tar.gz
