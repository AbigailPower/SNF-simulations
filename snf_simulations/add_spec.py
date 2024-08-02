import ROOT

import numpy as np

def add_spec(spectra):

    #adding spectra and setting limit to beyond the highest antineutrino energy in the database

    for i in range(len(spectra)):
        spectra[i].GetXaxis().SetLimits(0, 6000)

    hsum = spectra[14].Clone("combined")
    hsum.Reset()

    hsum.Merge(spectra)
    hsum.SetTitle("Total Spectrum")
 
    return hsum



    
