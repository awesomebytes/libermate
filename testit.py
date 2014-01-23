import sys
sys.path.append('Tests2')

from numpy import *
import scipy
import matcompat

from derivate import derivate

print derivate(array([r_[1.,2.,1.]]))



