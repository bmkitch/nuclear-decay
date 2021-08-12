import math

permitivity = 8.8541878128E-12 #permitivity of free space
c = 2.99E8 #speed of light
h = 1.055E-34 #Dirac constant
charge = 1.6E-19 #elementary charge

#estimates the mass of the beta stable line given the atomic charge
def betaLine(z):
    return 1.41867*math.pow(z, 1.12769) + 1.47124

#calculates coulomb barrier height from charge z and mass a
def b(z, a): 
    return 6.242E12 * (2 * (z - 2) * charge ** 2) / (4 * math.pi * permitivity * 1.25 * (math.pow(a, 1/3) / 1E15))

#predicts alpha Q energy on charge z and mass a. returns rough estimate. Inaccurate for many nuclei
def q(z, a): 
    return 28.3 - 4*15.5 + (8/3)*16.8*math.pow(a, -(1/3)) + 4*0.72*z*math.pow(a, -(1/3))*(1 - z/(3*a)) - 4*23*(1 - (2*z)/a)**2 + 3*34*math.pow(a, -(7/4))

#calculates gamow factor. a: atomic mass units, z: atomic charge, q: MEV, b: MEV. Most accurate when q is observed value.
def gamow(a, z, q, b): 
    m = (a/9.223E18) * 1.5E3
    return math.sqrt((2 * m) / (h ** 2 * q)) * ((2 * (z - 2) * charge ** 2) / (4 * math.pi * permitivity)) * ((math.pi / 2) - 2 * math.sqrt(q / b))

#calculates the probability of the alpha particle penetrating the barrier
def prob(gamow): 
    return math.exp(-2 * gamow)

#calculates the theoretical half-life
def halfLife(a, z, q):
    return 0.5 / (6E21 * prob(gamow(a, z, q, b(z, a))))