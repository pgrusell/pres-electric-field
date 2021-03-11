N_events = 33

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


hR = ROOT.TH2F("hR",";Z_{in}, mm;R_{in},mm",28,0,290,24,0,250)
hr = ROOT.TH1F("hr","dr", 500, -0.01, 0.99)

#for inZi in progress_bar( range( 28 ) ):
for inZi in range( 28 ) :
    inZ = 5.+10.*inZi
    for inRi in range( 24 ):
        inR = 5.+10.*inRi
        hr.Reset()
        for ev in  range(N_events) :
            phi = 2.*pi*random()
            inX = inR*cos(phi)
            inY = inR*sin(phi)
            pos, track_length = trace(inX, inY, inZ )
            outX, outY = pos.x(), pos.y()
            hr.Fill( sqrt((outX-inX)**2+(outY-inY)**2) )
        hR[ (inZi+1,inRi+1) ] = VE( hr.mean(),hr.rms()**2 )
        print("Z="+str(inZ)+"\tR="+str(inR)+"\tdr="+str(hr.mean()))

hR.GetZaxis().SetRangeUser(0,1.)
hR.Draw("colz")


