import math

#semi-empiracal binding energy formula
def binding(z, a):
    if(z % 2 == 0 and a % 2 == 0):
        p = 34 * math.pow(a, -3/4)
    elif(z % 2 != 0 and a % 2 == 0):
        p = -34 * math.pow(a, -3/4)
    else:
        p = 0

    return 15.5 * a - 16.8 * math.pow(a, 2/3) - 0.7 * z * (z - 1) * math.pow(a, -1/3) - 23 * (a - 2*z)**2 / a + p

#semi-empirical mass formula
def mass(z, a):
    return z * 1.00727647 + (a - z) * 1.008665 - binding(z, a) / 931.494061