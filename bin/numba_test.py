#!/bin/python3.10
# -*- coding: utf-8 -*-
import sys
#sys.path.append("/drop/.local/lib/python3.10/site-packages")
from numba import njit, cuda, prange
import numpy as np
import pandas as pd

import math
import pyarrow.csv as pa_csv
from typing import Tuple
import argparse
import time
import os
import re
import gc

#import numba

# Use numba.njit instead of directly importing njit
# @numba.njit
@njit(nopython=True)
def multiply(a, b):
    return a * b

# Test the function
# print("Numba version:", numba.__version__)
print("Result of multiply(4, 5):", multiply(4, 5))
