#inR = 34.
#inR = 154.
inR = 210.
inZ = 280.
#inZ = 290./2.
#inZ = 20.


#=====================================================================================


rfile = ROOT.TFile('histo.root',"READ")
h3_Ex = rfile["h3_Ex"]
h3_Ey = rfile["h3_Ey"]
h3_Ez = rfile["h3_Ez"]

from math import pi, sin, cos, tan, sqrt
from statistics import mean, stdev
from random import random
from   ostap.utils.progress_bar import progress_bar


def trace( x, y, z, step = 0.1, field = (True, True, True) ):
    track_length = 0.
    pos  = ROOT.TVector3( x, y, z )
    vect = ROOT.TVector3()
    while pos.z()>0 :
        x = pos.x()
        y = pos.y()
        z = pos.z()
        if field[0]:
            vect.SetX( h3_Ex(x,y,z).value() )
        if field[1]:
            vect.SetY( h3_Ey(x,y,z).value() )
        if field[2]:
            vect.SetZ( h3_Ez(x,y,z).value() )
        track_length += step
        pos  = pos + step*vect.Unit()

    factor = (pos - step*vect.Unit()).z() / step*vect.Unit().z()
    # this factor is negative as enumerator is positive and denominator is negative
    # that's why it's added at next steps
    pos  = pos - (1.+factor)*step*vect.Unit()
    track_length -= step*(1.+factor)
    return pos, track_length


hl = ROOT.TH1F("hl","length - z", 200, -0.01, 2.9)
hn = ROOT.TH1F("hl","length - z", 200, -0.01, 2.9)
hn.SetLineColor(2)

hr = ROOT.TH1F("hr","dr", 500, -0.01, 0.99)
ht = ROOT.TH1F("ht","dr", 500, -0.01, 0.99)
ht.SetLineColor(2)


h_dir = ROOT.TH2F("h_dir",";#phi_{in};#phi_{shift}",100, -pi, pi, 100, -pi, pi)

vdir = ROOT.TVector3()

for ev in progress_bar( range(330) ):
    phi = 2.*pi*(random()-0.5)
    inX = inR*cos(phi)
    inY = inR*sin(phi)
    pos, track_length = trace(inX, inY, inZ )
    outX, outY = pos.x(), pos.y()
    dr = sqrt((outX-inX)**2+(outY-inY)**2)
    vdir.SetXYZ( outX-inX, outY-inY, 0.)
    h_dir.Fill( phi, vdir.Phi() )
    #print( str(outX) + "  " +str(inX) + "  "+ str(outY) + "  "+str(inY) + "     "+str(phi))
    hl.Fill( 1000.*(track_length-inZ) )
    hr.Fill( dr )
    pos, track_length = trace(inX, inY, inZ , field=(False,False,True) )
    outX, outY = pos.x(), pos.y()
    dr = sqrt((outX-inX)**2+(outY-inY)**2)
    hn.Fill( 1000.*(track_length-inZ) )
    ht.Fill( dr )

hr.Draw()
ht.Draw("same")

h_dir.GetXaxis().SetTitleSize(0.04)
h_dir.GetYaxis().SetTitleSize(0.04)
h_dir.Draw("col")

rfile.Close()


