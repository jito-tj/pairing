"""
pairing
analyze pairing and clustering of molecular systems
"""

# Make Python 2 and 3 imports work the same
# Safe to remove with Python 3-only code
from __future__ import absolute_import

# Add imports here
from .pairing import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
