# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""MSTICPy Data Processing Tools."""

from .._version import VERSION

# flake8: noqa: F401
from . import base64unpack as base64
from . import process_tree_utils as ptree

__version__ = VERSION
