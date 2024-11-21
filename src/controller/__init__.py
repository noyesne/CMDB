# __init__.py

# Define the package version
__version__ = "1.0.0"



# Import specific modules from the package
from retrieve import _gather_info_

# Define what should be imported with `from package import *`
__all__ = ["_gather_info_"]