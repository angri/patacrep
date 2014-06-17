"""Global variables."""

from pkg_resources import resource_filename
import os
import sys

# Version
__VERSION__ = (3, 7, 2)
__STR_VERSION__ = '.'.join([str(number) for number in __VERSION__])

# Directory containing shared data (default templates, custom LaTeX packages,
# etc.)	
try:
    __DATADIR__ = os.path.abspath(resource_filename(__name__, 'data'))
except NotImplementedError:
    # if current module is frozen, use library.zip path for __DATADIR__ path
    if hasattr(sys,'frozen'):
        __DATADIR__ = os.path.join(os.path.dirname(__file__), 'data')
    else:
        raise IOError("coin")

