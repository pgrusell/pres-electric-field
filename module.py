import ROOT
from math import sqrt
import scipy.stats as stats



def VE(mean, var):
	std = sqrt(var)	/ 100
	return stats.norm.rvs(mean, mean * std)


	
def trace( x, y, z, h3_Ex, h3_Ey, h3_Ez, step = 0.1, field = (True, True, True)):
    track_length = 0.
    pos  = ROOT.TVector3( x, y, z )
    vect = ROOT.TVector3()
    while pos.z()>0 :
        x = pos.x()
        y = pos.y()
        z = pos.z()
        if field[0]:
            vect.SetX(h3_Ex.GetBinContent(h3_Ex.FindBin(x,y,z)))
        if field[1]:
            vect.SetY(h3_Ey.GetBinContent(h3_Ey.FindBin(x,y,z)))
        if field[2]:
            vect.SetZ(h3_Ez.GetBinContent(h3_Ez.FindBin(x,y,z)))
        track_length += step
        pos  = pos + step*vect.Unit()

    factor = (pos - step*vect.Unit()).z() / step*vect.Unit().z()
    # this factor is negative as enumerator is positive and denominator is negative
    # that's why it's added at next steps
    pos  = pos - (1.+factor)*step*vect.Unit()
    track_length -= step*(1.+factor)
    return pos, track_length
