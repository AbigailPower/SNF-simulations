import ROOT
import numpy as np

def scale(spectrum, m, mr, half_life_yrs, removal_time):
    #mass is inputted in kg
    #removal time is in years

    #calculation of activity of isotope
    N0 = (m* 1000 / mr) * 6.022e23
    A0 = N0 * (np.log(2) / (half_life_yrs *365 * 24 * 60**2))
    A = A0 * np.exp(-1 * (np.log(2) / half_life_yrs) * removal_time)
	
    spectrum.SetStats(0)

    spectrum.Scale(A) 

    spectrum.SetTitle("Scaled Spectrum")
    spectrum.GetXaxis().SetTitle("Energy [keV]")
    spectrum. GetYaxis().SetTitle("Relative Flux [keV^{-1}s^{-1}]")

    return spectrum
