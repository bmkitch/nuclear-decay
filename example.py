import betaDecay
import spontaneousFission as sf
import generalFunctions as gf
from matplotlib import pyplot as plt
from matplotlib import colors


#Shows energy released when the nucleus is streched into an ellipsoid. A positive energy release indicates instantaneous fission.
def fissionMap(zMin, zMax, aMin, aMax):
    isotopes = []
    for z in range(zMin, zMax):
        temp = []
        for a in range(aMin, aMax):
            if(betaDecay.betaMinusMassChange(z, a) > 0 and betaDecay.betaPlusMassChange(z, a) > 0):
                #temp.append(1/betaDecay.betaMinusMassChange(z, a))
                temp.append(1000)

            else:
                temp.append(sf.ellipsoidEnergyDifference(z, a))
        isotopes.append(temp)
    plt.imshow(isotopes, cmap='magma', origin='lower', extent=[aMin, aMax, zMin, zMax], vmax=100, vmin=-100) #norm=colors.LogNorm
    plt.show()

#Shows the theoretical point where neutrons or protons are emitted from the nucleus. Experimentation shows real
#driplines are much closer to the beta stable line.
def dripLine(zMin, zMax, aMin, aMax):
    isotopes = []
    for z in range(zMin, zMax):
        temp = []
        for a in range(aMin, aMax):
            if(-betaDecay.betaMinusMassChange(z, a) > gf.binding(z, a)):
                temp.append(1)
            else:
                temp.append(0)
            if(betaDecay.betaMinusMassChange(z, a) > 0 and betaDecay.betaPlusMassChange(z, a) > 0):
                temp[a - aMin] = 2
        isotopes.append(temp)
    
    plt.imshow(isotopes, cmap='magma', origin='lower', extent=[aMin, aMax, zMin, zMax], vmax=2, vmin=0)
    plt.show()

#Shows 1/mass-change of beta decay.
def visualBetaDecay(zMin, zMax, aMin, aMax):
    isotopes = []
    for z in range(zMin, zMax):
        temp = []
        for a in range(aMin, aMax):
            temp.append(0)
            #if(betaDecay.betaMinusMassChange(z, a) > 0 and betaDecay.betaPlusMassChange(z, a) > 0):
             #   temp[a - aMin] = 100000
            if(betaDecay.betaPlusMassChange(z, a) < betaDecay.betaMinusMassChange(z, a)):
                temp[a - aMin] = -1/betaDecay.betaPlusMassChange(z, a)
            else:
                temp[a - aMin] = -1/betaDecay.betaMinusMassChange(z, a)
        
        isotopes.append(temp)
    
    plt.imshow(isotopes, cmap='magma', origin='lower', extent=[aMin, aMax, zMin, zMax], norm=colors.LogNorm())
    plt.show()