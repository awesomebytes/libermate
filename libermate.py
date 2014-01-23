#!/usr/bin/env python
#
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
__version__ = "0.1"
__copyright__ = "Copyright (c) 2009 Eric C. Schug"
__license__ = "GNU General Public License"
__revision__ = "$Id$"

# Standard Python
import sys
import re
from copy import copy
import glob
import os
import stat
import pprint

import clips

has_syck=False
try:
    import syck
    has_syck=True
    class DumpNoTuple(syck.Dumper):
        def represent_tuple(self, object):
            return _syck.Seq(list(object), tag="tag:python.yaml.org,2002:seq")

except ImportError:
    pass

### class "calcLexer extends Lexer" will generate python
### module "calcLexer" with class "Lexer". 
import MatlabLexer
import MatlabParser
import Mat2Py
import translate_new

import antlr
import CommandLine
import BaseRules


def ASTtoTree(ast):
    'Build'
    a=ast
    b=[]
    while a:
        c=ASTtoTree(a.getFirstChild())
        node=BaseRules.ASTNode(a.getType(), a.getText(), c)
        b.append(node)
        a=a.getNextSibling()
    return b

python_priority = {
    "": -4,
    "=": -3,
    ",": -1,
    ":": 0,
    "lambda": 0,
    "or": 1,
    "and": 2,
    "not": 3,
    ">": 6,
    "<": 6,
    "<=": 6,
    ">=": 6,
    "==": 6,
    "!=": 6,
    "|": 7,
    "^": 8,
    "&": 9,
    "+": 11,
    "-": 11,
    "*": 12,
    "/": 12,
    " +": 13,
    " -": 13,
    "~": 14,
    "**": 15,
    ".": 16,
    "x(":17, 
    "NAME": 18, 
    "VAR": 18, 
    }
    
# n = numel(A) returns the number of elements, n, in array A.

class MatParse(MatlabParser.Parser):
    'Higher level logic for parser'
    def __init__(self, *args, **kwargs):
        MatlabParser.Parser.__init__(self, *args, **kwargs)
        self.vars=set()
        self.funcs=set()
        self.is_dot=False
        self.inside_args=False
    def new_scope(self):
        'Create a new function scope'
        self.vars=set()
        self.funcs=set()

    def get_scope(self):
        'Get current scope'
        ast=self.astFactory.create(MatlabParser.SCOPE,", ".join(self.vars)+"\n    # Function calls: "+", ".join(self.funcs))
        print 'The following appear to be variables:'
        print '  ',", ".join(self.vars)
        print 'The following appear to be functions:'
        print '  ',", ".join(self.funcs)
        return ast
    def as_global(self,vartoken):
        'add variable as a global'
        vartoken.setType(MatlabParser.VAR)
        self.vars.add(vartoken.getText())
    def as_persistant(self,vartoken):
        'add variable as a persistant'
        vartoken.setType(MatlabParser.VAR)
        self.vars.add(vartoken.getText())
    def as_var(self,vartoken):
        'NAME token is a variable'
        vartoken.setType(MatlabParser.VAR)
        self.vars.add(vartoken.getText())
    def as_func(self,functoken):
        'NAME token is a function'
        self.funcs.add(functoken.getText())
        
    def var_lookup(self,vartoken):
        'Lookup NAME token in scope and set type'
        #print("Checking var",vartoken.getText())
        if(self.is_dot or (vartoken.getText() in self.vars)):
            vartoken.setType(MatlabParser.VAR)
        else:
            self.as_func(vartoken)
    def var_names(self):
        return list(self.vars)
    def print_tree(self,tree):
        pprint.pprint(ASTtoTree(tree))
        sys.stdout.flush()
numpy_names=['abs', 'absolute', 'add', 'add_docstring', 'add_newdoc', 'add_newdocs', 'alen', 'all', 'allclose', 'alltrue', 'alterdot', 'amax', 'amin', 'angle', 'any', 'append', 'apply_along_axis', 'apply_over_axes', 'arange', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'argmax', 'argmin', 'argsort', 'argwhere', 'around', 'array', 'array2string', 'array_equal', 'array_equiv', 'array_repr', 'array_split', 'array_str', 'asanyarray', 'asarray', 'asarray_chkfinite', 'ascontiguousarray', 'asfarray', 'asfortranarray', 'asmatrix', 'asscalar', 'atleast_1d', 'atleast_2d', 'atleast_3d', 'average', 'bartlett', 'base_repr', 'binary_repr', 'bincount', 'bitwise_and', 'bitwise_not', 'bitwise_or', 'bitwise_xor', 'blackman', 'bmat', 'bool', 'bool8', 'bool_', 'broadcast', 'byte', 'byte_bounds', 'c_', 'can_cast', 'cast', 'cdouble', 'ceil', 'cfloat', 'char', 'character', 'chararray', 'choose', 'clip', 'clongdouble', 'clongfloat', 'column_stack', 'common_type', 'compare_chararrays', 'complex', 'complex128', 'complex192', 'complex64', 'complex_', 'complexfloating', 'compress', 'concatenate', 'conj', 'conjugate', 'convolve', 'copy', 'core', 'corrcoef', 'correlate', 'cos', 'cosh', 'cov', 'cross', 'csingle', 'ctypeslib', 'cumprod', 'cumproduct', 'cumsum', 'delete', 'deprecate', 'diag', 'diagflat', 'diagonal', 'diff', 'digitize', 'disp', 'distutils', 'divide', 'dot', 'double', 'dsplit', 'dstack', 'dtype', 'e', 'ediff1d', 'emath', 'empty', 'empty_like', 'equal', 'errstate', 'exp', 'expand_dims', 'expm1', 'extract', 'eye', 'fabs', 'fastCopyAndTranspose', 'fft', 'finfo', 'fix', 'flatiter', 'flatnonzero', 'flexible', 'fliplr', 'flipud', 'float', 'float32', 'float64', 'float96', 'float_', 'floating', 'floor', 'floor_divide', 'fmod', 'format_parser', 'frexp', 'frombuffer', 'fromfile', 'fromfunction', 'fromiter', 'frompyfunc', 'fromstring', 'generic', 'get_array_wrap', 'get_include', 'get_numarray_include', 'get_numpy_include', 'get_printoptions', 'getbuffer', 'getbufsize', 'geterr', 'geterrcall', 'geterrobj', 'gradient', 'greater', 'greater_equal', 'hamming', 'hanning', 'histogram', 'histogram2d', 'histogramdd', 'hsplit', 'hstack', 'hypot', 'i0', 'identity', 'iinfo', 'imag', 'index_exp', 'indices', 'inexact', 'inf', 'info', 'infty', 'inner', 'insert', 'int', 'int0', 'int16', 'int32', 'int64', 'int8', 'int_', 'int_asbuffer', 'intc', 'integer', 'interp', 'intersect1d', 'intersect1d_nu', 'intp', 'invert', 'iscomplex', 'iscomplexobj', 'isfinite', 'isfortran', 'isinf', 'isnan', 'isneginf', 'isposinf', 'isreal', 'isrealobj', 'isscalar', 'issctype', 'issubclass_', 'issubdtype', 'issubsctype', 'iterable', 'ix_', 'kaiser', 'kron', 'ldexp', 'left_shift', 'less', 'less_equal', 'lexsort', 'lib', 'linalg', 'linspace', 'little_endian', 'load', 'loads', 'loadtxt', 'log', 'log10', 'log1p', 'log2', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'logspace', 'long', 'longcomplex', 'longdouble', 'longfloat', 'longlong', 'ma', 'mat', 'math', 'matrix', 'max', 'maximum', 'maximum_sctype', 'may_share_memory', 'mean', 'median', 'memmap', 'meshgrid', 'mgrid', 'min', 'minimum', 'mintypecode', 'mod', 'modf', 'msort', 'multiply', 'nan', 'nan_to_num', 'nanargmax', 'nanargmin', 'nanmax', 'nanmin', 'nansum', 'nbytes', 'ndarray', 'ndenumerate', 'ndim', 'ndindex', 'negative', 'newaxis', 'newbuffer', 'nonzero', 'not_equal', 'number', 'obj2sctype', 'object', 'object0', 'object_', 'ogrid', 'oldnumeric', 'ones', 'ones_like', 'outer', 'pi', 'piecewise', 'pkgload', 'place', 'poly', 'poly1d', 'polyadd', 'polyder', 'polydiv', 'polyfit', 'polyint', 'polymul', 'polysub', 'polyval', 'power', 'prod', 'product', 'ptp', 'put', 'putmask', 'r_', 'random', 'rank', 'ravel', 'real', 'real_if_close', 'rec', 'recarray', 'reciprocal', 'record', 'remainder', 'repeat', 'require', 'reshape', 'resize', 'restoredot', 'right_shift', 'rint', 'roll', 'rollaxis', 'roots', 'rot90', 'round', 'round_', 'row_stack', 's_', 'savetxt', 'sctype2char', 'sctypeDict', 'sctypeNA', 'sctypes', 'searchsorted', 'select', 'set_numeric_ops', 'set_printoptions', 'set_string_function', 'setbufsize', 'setdiff1d', 'seterr', 'seterrcall', 'seterrobj', 'setmember1d', 'setxor1d', 'shape', 'short', 'show_config', 'sign', 'signbit', 'signedinteger', 'sin', 'sinc', 'single', 'singlecomplex', 'sinh', 'size', 'sometrue', 'sort', 'sort_complex', 'source', 'split', 'sqrt', 'square', 'squeeze', 'std', 'str', 'str_', 'string0', 'string_', 'subtract', 'sum', 'swapaxes', 'take', 'tan', 'tanh', 'tensordot', 'test', 'testing', 'tile', 'trace', 'transpose', 'trapz', 'tri', 'tril', 'trim_zeros', 'triu', 'true_divide', 'typeDict', 'typeNA', 'typecodes', 'typename', 'ubyte', 'ufunc', 'uint', 'uint0', 'uint16', 'uint32', 'uint64', 'uint8', 'uintc', 'uintp', 'ulonglong', 'unicode', 'unicode0', 'unicode_', 'union1d', 'unique', 'unique1d', 'unravel_index', 'unsignedinteger', 'unwrap', 'ushort', 'vander', 'var', 'vdot', 'vectorize', 'version', 'void', 'void0', 'vsplit', 'vstack', 'where', 'who', 'zeros', 'zeros_like']


pylab_names=['absolute', 'acorr', 'add', 'add_docstring', 'add_newdoc', 'add_newdocs', 'alen', 'all', 'allclose', 'alltrue', 'alterdot', 'amap', 'amax', 'amin', 'angle', 'annotate', 'any', 'append', 'apply_along_axis', 'apply_over_axes', 'approx_real', 'arange', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'argmax', 'argmin', 'argsort', 'argwhere', 'around', 'array', 'array2string', 'array_equal', 'array_equiv', 'array_repr', 'array_split', 'array_str', 'arrow', 'asanyarray', 'asarray', 'asarray_chkfinite', 'ascontiguousarray', 'asfarray', 'asfortranarray', 'asmatrix', 'asscalar', 'atleast_1d', 'atleast_2d', 'atleast_3d', 'autumn', 'average', 'axes', 'axhline', 'axhspan', 'axis', 'axvline', 'axvspan', 'bar', 'barh', 'bartlett', 'base_repr', 'beta', 'binary_repr', 'bincount', 'binomial', 'bitwise_and', 'bitwise_not', 'bitwise_or', 'bitwise_xor', 'bivariate_normal', 'blackman', 'bmat', 'bone', 'bool8', 'bool_', 'box', 'boxplot', 'broadcast', 'broken_barh', 'byte', 'byte_bounds', 'bytes', 'c_', 'can_cast', 'cast', 'cdouble', 'ceil', 'center_matrix', 'cfloat', 'char', 'character', 'chararray', 'chisquare', 'cholesky', 'choose', 'cla', 'clabel', 'clf', 'clim', 'clip', 'clongdouble', 'clongfloat', 'close', 'cm', 'cohere', 'colorbar', 'colorbar_doc', 'colormaps', 'colors', 'column_stack', 'common_type', 'compare_chararrays', 'complex128', 'complex192', 'complex64', 'complex_', 'complexfloating', 'compress', 'concatenate', 'conj', 'conjugate', 'connect', 'contour', 'contourf', 'conv', 'convolve', 'cool', 'copper', 'copy', 'corrcoef', 'correlate', 'cos', 'cosh', 'cov', 'cross', 'csd', 'csingle', 'csv2rec', 'ctypeslib', 'cumprod', 'cumproduct', 'cumsum', 'date2num', 'datestr2num', 'dedent', 'delaxes', 'delete', 'demean', 'deprecate', 'det', 'detrend', 'detrend_linear', 'detrend_mean', 'detrend_none', 'diag', 'diagflat', 'diagonal', 'diagonal_matrix', 'diff', 'digitize', 'disconnect', 'disp', 'dist', 'dist_point_to_segment', 'divide', 'dot', 'double', 'drange', 'draw', 'draw_if_interactive', 'dsplit', 'dstack', 'dtype', 'e', 'ediff1d', 'eig', 'eigh', 'eigvals', 'eigvalsh', 'emath', 'empty', 'empty_like', 'entropy', 'enumerate', 'epoch2num', 'equal', 'errorbar', 'errstate', 'exception_to_str', 'exp', 'exp_safe', 'expand_dims', 'expm1', 'exponential', 'extract', 'eye', 'f', 'fabs', 'fastCopyAndTranspose', 'fft', 'fft2', 'fftfreq', 'fftn', 'fftpack', 'fftpack_lite', 'fftshift', 'fftsurr', 'figaspect', 'figimage', 'figlegend', 'figtext', 'figure', 'fill', 'find', 'finfo', 'fix', 'flag', 'flatiter', 'flatnonzero', 'flatten', 'flexible', 'fliplr', 'flipud', 'float32', 'float64', 'float96', 'float_', 'floating', 'floor', 'floor_divide', 'fmod', 'format_parser', 'frange', 'frexp', 'frombuffer', 'fromfile', 'fromfunction', 'fromfunction_kw', 'fromiter', 'frompyfunc', 'fromstring', 'gamma', 'gca', 'gcf', 'gci', 'generic', 'geometric', 'get', 'get_array_wrap', 'get_backend', 'get_cmap', 'get_current_fig_manager', 'get_include', 'get_numarray_include', 'get_numpy_include', 'get_plot_commands', 'get_printoptions', 'get_sparse_matrix', 'get_state', 'get_xyz_where', 'getbuffer', 'getbufsize', 'geterr', 'geterrcall', 'geterrobj', 'getp', 'gradient', 'gray', 'greater', 'greater_equal', 'grid', 'gumbel', 'hamming', 'hanning', 'helper', 'hfft', 'hist', 'histogram', 'histogram2d', 'histogramdd', 'hlines', 'hold', 'hot', 'hsplit', 'hstack', 'hsv', 'hypergeometric', 'hypot', 'i0', 'identity', 'ifft', 'ifft2', 'ifftn', 'ifftshift', 'ihfft', 'iinfo', 'imag', 'imread', 'imshow', 'index_exp', 'indices', 'inexact', 'inf', 'info', 'infty', 'inner', 'insert', 'inside_poly', 'int0', 'int16', 'int32', 'int64', 'int8', 'int_', 'int_asbuffer', 'intc', 'integer', 'interp', 'intersect1d', 'intersect1d_nu', 'intp', 'inv', 'invert', 'ioff', 'ion', 'irefft', 'irefft2', 'irefftn', 'irfft', 'irfft2', 'irfftn', 'is_numlike', 'is_string_like', 'iscomplex', 'iscomplexobj', 'isfinite', 'isfortran', 'ishold', 'isinf', 'isinteractive', 'isnan', 'isneginf', 'isposinf', 'ispower2', 'isreal', 'isrealobj', 'isscalar', 'issctype', 'issubclass_', 'issubdtype', 'issubsctype', 'iterable', 'ix_', 'jet', 'kaiser', 'kron', 'l1norm', 'l2norm', 'lapack_lite', 'laplace', 'ldexp', 'left_shift', 'legend', 'less', 'less_equal', 'levypdf', 'lexsort', 'liaupunov', 'linalg', 'linspace', 'little_endian', 'load', 'loads', 'loadtxt', 'log', 'log10', 'log1p', 'log2', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'logistic', 'loglog', 'lognormal', 'logseries', 'logspace', 'longcomplex', 'longdouble', 'longest_contiguous_ones', 'longest_ones', 'longfloat', 'longlong', 'lstsq', 'ma', 'mat', 'math', 'matplotlib', 'matrix', 'matshow', 'maximum', 'maximum_sctype', 'may_share_memory', 'mean', 'mean_flat', 'median', 'memmap', 'meshgrid', 'mfuncC', 'mgrid', 'minimum', 'mintypecode', 'mlab', 'mod', 'modf', 'movavg', 'mpl', 'msort', 'multinomial', 'multiply', 'multivariate_normal', 'mx2num', 'nan', 'nan_to_num', 'nanargmax', 'nanargmin', 'nanmax', 'nanmin', 'nansum', 'nbytes', 'ndarray', 'ndenumerate', 'ndim', 'ndindex', 'negative', 'negative_binomial', 'new_figure_manager', 'newaxis', 'newbuffer', 'noncentral_chisquare', 'noncentral_f', 'nonzero', 'norm', 'norm_flat', 'normal', 'normalize', 'normpdf', 'not_equal', 'npy', 'num2date', 'num2epoch', 'number', 'obj2sctype', 'object0', 'object_', 'ogrid', 'ones', 'ones_like', 'orth', 'outer', 'over', 'pareto', 'pcolor', 'pcolormesh', 'permutation', 'pi', 'pie', 'piecewise', 'pink', 'pinv', 'pkgload', 'place', 'plot', 'plot_date', 'plotfile', 'plotting', 'poisson', 'polar', 'poly', 'poly1d', 'poly_below', 'poly_between', 'polyadd', 'polyder', 'polydiv', 'polyfit', 'polyint', 'polymul', 'polysub', 'polyval', 'popd', 'power', 'prctile', 'prctile_rank', 'prepca', 'prism', 'prod', 'product', 'psd', 'ptp', 'put', 'putmask', 'pylab_setup', 'qr', 'quiver', 'quiverkey', 'r_', 'rand', 'randint', 'randn', 'random', 'random_integers', 'random_sample', 'ranf', 'rank', 'ravel', 'rayleigh', 'rc', 'rcParams', 'rcParamsDefault', 'rcdefaults', 'real', 'real_if_close', 'rec', 'rec2csv', 'rec_append_field', 'rec_drop_fields', 'rec_join', 'recarray', 'reciprocal', 'record', 'refft', 'refft2', 'refftn', 'relativedelta', 'rem', 'remainder', 'repeat', 'require', 'reshape', 'resize', 'restoredot', 'rfft', 'rfft2', 'rfftn', 'rgrids', 'right_shift', 'rint', 'rk4', 'rms_flat', 'roll', 'rollaxis', 'roots', 'rot90', 'round_', 'row_stack', 'rrule', 's_', 'sample', 'save', 'savefig', 'savetxt', 'scatter', 'sci', 'sctype2char', 'sctypeDict', 'sctypeNA', 'sctypes', 'searchsorted', 'seed', 'segments_intersect', 'select', 'semilogx', 'semilogy', 'set_numeric_ops', 'set_printoptions', 'set_state', 'set_string_function', 'setbufsize', 'setdiff1d', 'seterr', 'seterrcall', 'seterrobj', 'setmember1d', 'setp', 'setxor1d', 'shape', 'short', 'show', 'show_config', 'shuffle', 'sign', 'signbit', 'signedinteger', 'silent_list', 'sin', 'sinc', 'single', 'singlecomplex', 'sinh', 'size', 'slopes', 'solve', 'sometrue', 'sort', 'sort_complex', 'source', 'specgram', 'spectral', 'split', 'spring', 'spy', 'sqrt', 'sqrtm', 'square', 'squeeze', 'standard_cauchy', 'standard_exponential', 'standard_gamma', 'standard_normal', 'standard_t', 'std', 'stem', 'step', 'stineman_interp', 'str_', 'string0', 'string_', 'strpdate2num', 'subplot', 'subplot_tool', 'subplots_adjust', 'subtract', 'sum', 'sum_flat', 'summer', 'svd', 'swapaxes', 'switch_backend', 'sys', 'table', 'take', 'tan', 'tanh', 'tensordot', 'tensorinv', 'tensorsolve', 'test', 'text', 'thetagrids', 'tile', 'title', 'trace', 'transpose', 'trapz', 'tri', 'triangular', 'tril', 'trim_zeros', 'triu', 'true_divide', 'twinx', 'twiny', 'typeDict', 'typeNA', 'typecodes', 'typename', 'ubyte', 'ufunc', 'uint', 'uint0', 'uint16', 'uint32', 'uint64', 'uint8', 'uintc', 'uintp', 'ulonglong', 'unicode0', 'unicode_', 'uniform', 'union1d', 'unique', 'unique1d', 'unravel_index', 'unsignedinteger', 'unwrap', 'ushort', 'vander', 'var', 'vdot', 'vectorize', 'vlines', 'void', 'void0', 'vonmises', 'vsplit', 'vstack', 'wald', 'warnings', 'weibull', 'where', 'who', 'window_hanning', 'window_none', 'winter', 'xcorr', 'xlabel', 'xlim', 'xticks', 'ylabel', 'ylim', 'yticks', 'zeros', 'zeros_like', 'zipf']

import keyword
class Mat2PyTrans(translate_new.Mat2Py):
    'Higher level logic for translator'
    def __init__(self):
        #Mat2Py.Walker.__init__(self)
        translate_new.Mat2Py.__init__(self)
        self.nl="\n"
        self.indcnt=0
        self.indent=""
        self.in_var=False
        self.is_simple_rhs=False
        self.is_lhs=False
        self.token_stack=[]
        # Define simple mapping of functions
        self.mapping={'size':'matcompat.size',
            'ndims':'matcompat.ndim',
            'eps':'finfo(float).eps',
            'i':'1j',
            'find':'nonzero',
            'rand':'np.random.rand',
            'meshgrid':'matcompat.meshgrid',
            'repmat':'matcompat.repmat',
            'max':'matcompat.max',
            'min':'matcompat.max',
            'error':'matcompat.error', 
            'warning':'matcompat.warning', 
            'norm':'linalg.norm',
            'bitand':'&Error',
            'bitor':'|Error',
            'inv':'linalg.inv',
            'pinv':'linalg.pinv',
            'chol':'linalg.cholesky',
            'eig':'linalg.eig',
            'qr':'scipy.linalg.qr',
            'lu':'scipy.linalg.lu',
            'conjgrad':'scipy.linalg.cg',
            'regress':'linalg.lstsqError',
            'decimate':'matcompat.decimate',
            'assert':'matcompat.assert',
            }
    def incr(self):
        'increment indent'
        self.indcnt+=1
        self.indent=" "*(self.indcnt*4)
        self.nl="\n"+self.indent
        #print 'increment "'+self.indent+'"'
    def decr(self):
        'decrement indent'
        self.indcnt-=1
        self.indent=" "*(self.indcnt*4)
        self.nl="\n"+self.indent
        #print 'decrement "'+self.indent+'"'
    def Lookup(self, name):
        'Do simple function mapping'
        if(name in self.mapping):
            return self.mapping[name]
        if(name in numpy_names):
            return 'np.'+name
        if(name in pylab_names):
            return 'plt.'+name
        if(keyword.iskeyword(name)):
            if(name!='assert'):
                name=name+'_rename'
        return name
    def bop(self, op, ptoken,  a, b, add_padding=False):
        'binary operator'
        if(add_padding):
            pad=' '
        else:
            pad=''
        if(not a):
            a='Error'
        if(not b):
            b='Error'
        k=a+pad+op.strip()+pad+b
        #print 'bop "%s"[%d] <- "%s"[%d] %s %s' % ( ptoken, python_priority[ptoken],  op, python_priority[op],  a,  b) 
        if(python_priority[ptoken]>python_priority[op]):
            #print '('+k+')'
            return '('+k+')'
        else:
            return k
    def preop(self, op, ptoken, a, add_padding=False):
        'Prefix operator'
        if(add_padding):
            pad=' '
        else:
            pad=''
        if(not a):
            a='Error'
        k=op.strip()+pad+a
        #print 'preop "%s"[%d] <- "%s"[%d] %s' % ( ptoken, python_priority[ptoken],  op, python_priority[op],  a) 
        if(python_priority[ptoken]>python_priority[op]):
            #print '('+k+')'
            return '('+k+')'
        else:
            return k
    def multiop(self, op, ptoken, c, add_padding=False):
        'multiple operator'
        if(add_padding):
            pad=' '
        else:
            pad=''
        k=(pad+op.strip()+pad).join(c)
        if(python_priority[ptoken]>python_priority[op]):
            return '('+k+')'
        else:
            return k
    def colonop(self, ptoken, cc):
        'colon operator'
        a=cc[0]
        b=cc[1]
        if(len(cc)>2):
            c=cc[2]
        else:
            c=None
        if( self.in_var):
            if(not a and not b):
                sstr=":"
            else:
                if(a.replace('.','').isdigit()):
                    a=str(int(float(a))-1)
                else:
                    a="int("+a+")-1"
                if(c):
                    if(c=='xend'):
                        c=''
                    sstr=a+":"+c+":"+b
                else:
                    if(b=='xend'):
                        b=''
                    sstr=a+":"+b
        else:
            if(not a and not b):
                sstr="Error:Error"
            else:
                if(c):
                    if(c.replace('.','').isdigit() and b.replace('.','').isdigit()):
                        c=str(float(c)+float(b))
                    else:
                        c="("+c+")+("+b+")"
                    sstr="np.arange("+a+", "+c+", "+b+")"
                else:
                    if(b.replace('.','').isdigit()):
                        b=str(float(b)+1)
                    else:
                        b="("+b+")+1"
                    sstr="np.arange("+a+", "+b+")"
        return sstr
        
    def join_args(self, cc, braces=False, ptoken=None):
        def mapper(ii):
            if(":" in ii):
                return ii
            elif(ii.isdigit()):
                return str(int(ii)-1)
            else:
                return 'int('+ii+')-1'
        if(self.in_var or self.is_lhs or ptoken=="VAR"):
            if(braces):
                sstr=".cell["
            else:
                sstr="["
            
            cc=[mapper(ii) for ii in cc]
            k=",".join(cc)
            if(k==':' and not self.is_lhs and not braces):
                return '.flatten(1)'
            else:
                sstr+=k
            if(braces):
                sstr+="]"
            else:
                sstr+="]"
        else:
            if(braces):
                sstr=".cell_getattr("+", ".join(cc)+")"
            else:
                sstr="("+", ".join(cc)+")"
        return sstr

default_header="""
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

"""

class MainApp(CommandLine.App):
    usage_str='[options] [matfile]...'
    about_str='Translates MATLAB file(s) matfile (.m) to Python files (.py)'

    def __init__(self):
         
        # Specify configuration options build an array of options defined as
        # [Name, shortkey, description, type, default]
        #type can be 'str','dir','file','bool','num', or a list of strings (enumeration)
        self.config_options=[
            ['help','h','display help and quit','bool',False],
            ['astdump','','dump Abstract Syntax Tree to file, .ast','bool',False],
            ['headerfile','','load header from ARG','file', None],
            #TODO ['output','o','log output to file ARG','file','libermate.log'],
            #TODO ['quite','','run silently hush all but prompts','bool',False],
        ]
        args=self.command_line()
        self.files=[]
        for ifile in args:
            #files=glob.glob(ifile)
            files=[ifile]
            self.files.extend(files)
        for filename in self.files:
            try:
                stat_info=os.stat(filename)
            except OSError, desc:
                print 'Error: could not open file %s' % filename
                sys.exit(2)
            if(stat.S_ISDIR(stat_info[stat.ST_MODE])):
                print 'Error: %s is a directory but should be a file' % filename
                sys.exit(2)
            if filename.replace('.m','.py') == filename:
                print "Error: file %s must have a .m suffix" % filename
                sys.exit(2)
                
        #print self.files
        self.main()
    def main(self):
        if(self.headerfile):
            f=open(self.headerfile)
            header=''.join(f.readlines())
            f.close()
        else:
            header=default_header
        for filename in self.files:
            print '\n'+'-'*20
            print 'Opening File', filename
            f = file(filename, "r")
            lexer = MatlabLexer.Lexer(f)          ### create a lexer for calculator
            print 'Starting Parser'
            p = MatParse(lexer)
            p.script()
            print 'Parser Complete'
            a = p.getAST()
            root = ASTtoTree(a)
            rules=BaseRules.BaseRules()
            for node in root:
                node.assert_all()
            #clips.PrintAgenda()
            #clips.SaveFacts(filename.replace('.m','.facts'))
            rules.run()
            #clips.SaveFacts(filename.replace('.m','.facts2'))
            
            if(self.astdump):
                outfile = filename.replace('.m', '.ast')
                print 'writing to file', outfile
                f = open(outfile, 'w')
                astlist=[node.to_list() for node in root]
                if(has_syck and False):
                    f.write(syck.dump(astlist, Dumper=DumpNoTuple))
                else:
                    f.write(pprint.pformat(astlist))
                f.close()
            if(0):
                outfile = filename.replace('.m', '.nast')
                print 'writing to file', outfile
                f=open(outfile, 'w')
                if(has_syck and False):
                    f.write(syck.dump(root, Dumper=DumpNoTuple))
                else:
                    f.write(pprint.pformat(root))
            
            walk = Mat2PyTrans()
            print "Starting Translator"
            s=walk.translate(root)
            #Simple conversions
            s=re.sub(r'pi\(\)','pi',s)
            s=re.sub(r'Inf\(\)','inf',s)
            s=re.sub(r'nan\(\)','nan',s)
            s=re.sub(r'int\(([\d]+)\.\)',r'\1',s)
            def sub_eval(m):
                return str(eval(m.group(1)))
            s=re.sub(r"np.random.rand\('state',","random.set_state(",s)
            #s=re.sub(r"random.rand\(\),","random.set_state(",s)
            s=re.sub(r'([\d]+\.?-1)',sub_eval,s)
            #s=re.sub(r'matdiv\((.+?),\ (\d+.)\)',r'(\1)/\2',s)
            #s=re.sub(r'matdiv\((\d+.),\ ',r'\1/(',s)
            #s=re.sub(r'np.dot\((.+?),\ (\d+.)\)',r'(\1)*\2',s)
            #s=re.sub(r'np.dot\((\d+.),\ ',r'\1*(',s)
            s=re.sub(r'shape\.Error\(([\w\.]+),\ ([\w\.]+)\)',r'\1.shape[\2-1]',s)
            s=re.sub(r'shape\.Error\((\w+)\)',r'\1.shape',s)
            s=re.sub(r'\.flatten\(1\)\.conj\(\)\.T',r'.flatten(0).conj()',s)
            s=re.sub(r'\.flatten\(1\)\.T',r'.flatten(0)',s)
            s=re.sub(r'\.flatten\(1\)\.T',r'.flatten(0)',s)
            s=re.sub(r'xend',r'0',s)
            print 'Translation Complete'
            #print p.var_names()
            
            outfile=filename.replace('.m', '.py')
            print 'writing to file', outfile
            f=open(outfile,'w')
            f.write( header )
            f.write(s)
            f.close()
        
def testLexer(files):
    'do quick scan of selected files'
    #files=glob.glob('/home/eric/Downloads/mpi-ikl-simplemkl-1.0/*.m')
    quick_scan(files)
    
def testLexer(filename):
    'test parsing of specified file'

    f = file(filename, "r")
    lexer = MatlabLexer.Lexer(f)          ### create a lexer for calculator
    pcount=0
    for token in lexer:
        ## do something with token
        print token.getText(),
        if token.getType() in [MatlabParser.END,MatlabParser.ARRAY_END,MatlabParser.STRING,MatlabParser.TRANS]:
            print "\\"+str(pcount)+MatlabParser._tokenNames[token.getType()]+'/',
        if(token.getType() in [MatlabParser.LPAREN,MatlabParser.LBRACE,MatlabParser.ATPAREN]):
            pcount+=1
            print '\\'+str(pcount)+'/',
        if(token.getType() in [MatlabParser.RPAREN,MatlabParser.RBRACE]):
            pcount-=1
            print '\\'+str(pcount)+'/',

def testParser(files):
    'Test parsing of specified files'
    
    for filename in files:
        f = file(filename, "r")
        lexer = MatlabLexer.Lexer(f)          ### create a lexer for calculator
        p = MatParse(lexer)
        p.script()
        a=p.getAST()
        b=ASTtoTree(a)

def  main():
    app=MainApp()

if __name__ == "__main__":
    main()
    
