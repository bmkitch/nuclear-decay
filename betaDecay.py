import math
from matplotlib import colors, pyplot as plt
import alphaDecay
import generalFunctions as gf

#returns the mass change of an atom after beta plus decay.
def betaPlusMassChange(z, a):
    return gf.mass(z - 1, a) - gf.mass(z, a)

#returns the mass change of an atom afer beta minus decay.
def betaMinusMassChange(z, a):
    return gf.mass(z + 1, a) - gf.mass(z, a)

#If the mass change is positive, then the atom won't undergo that decay type.
#If both decay types are positive, then the atom is beta stable.