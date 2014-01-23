# LiberMate
#
# Copyright (C) 2009  Eric C. Schug
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__author__ = "Eric C. Schug (schugschug@gmail.com)"
__copyright__ = "Copyright (c) 2009 Eric C. Schug"
__license__ = "GNU General Public License"
__revision__ = "$Id$"

import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

import types

#does structure have attribute/field name 
def isfield(struct,name):
    return hasattr(struct,name)


class MatError(Exception):
    pass

def error(mesg):
    raise MatError, mesg

class MatWarning(UserWarning):
    pass

def warning(mesg):
    raise MatWarning, mesg

def length(x):
    len(x.flatten())

def size(mat, elem=None):
    if not elem:
        return mat.shape
    else:
        return mat.shape[int(elem)-1]
