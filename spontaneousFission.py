import math
import generalFunctions

#Returns the coulomb barrier height of two touching nuclei in mevs.
def barrierHeight(z, a):
   return 1.44 * (z/2)**2 / (2 * (1.25 * math.pow(a/2, 1/3)))

#The energy difference in mevs between a streched necleus and a spherical nucleus. Nucleus undergoes fission if the difference is positive.
def ellipsoidEnergyDifference(z, a):
    return -0.4 * 16.8 * math.pow(a, 2 / 3) + 0.2 * 0.7 * (z**2) * math.pow(a, -1/3)

#Returns the energy released in nuclear fission in mevs.
def fissionRelease(z, a):
    return 2 * generalFunctions.binding(z/2, a/2) - generalFunctions.binding(z, a)