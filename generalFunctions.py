import math

#estimates the mass of the beta stable line given the atomic charge
def betaLine(z):
    return 1.41867*math.pow(z, 1.12769) + 1.47124