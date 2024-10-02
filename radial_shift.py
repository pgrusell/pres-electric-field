import ROOT
from module import *
from math import pi, sin, cos, tan, sqrt
from statistics import mean, stdev
from random import random
from   ostap.utils.progress_bar import progress_bar

N_events = 33

rfile = ROOT.TFile('histo.root',"READ")

h3_Ex = rfile.Get("h3_Ex")
h3_Ey = rfile.Get("h3_Ey")
h3_Ez = rfile.Get("h3_Ez")

hR = ROOT.TH2F("hR",";Z_{in}, mm;R_{in},mm",28,0,290,24,0,250)
hr = ROOT.TH1F("hr","dr", 500, -0.01, 0.99)

for inZi in range( 28 ) :
    inZ = 5.+10.*inZi
    for inRi in range( 24 ):
        inR = 5.+10.*inRi
        hr.Reset()
        for ev in  range(N_events) :
            phi = 2.*pi*random()
            inX = inR*cos(phi)
            inY = inR*sin(phi)
            pos, track_length = trace(inX, inY, inZ, h3_Ex, h3_Ey, h3_Ez)
            outX, outY = pos.x(), pos.y()
            hr.Fill( sqrt((outX-inX)**2+(outY-inY)**2) )
        hR.SetBinContent(inZi+1,inRi+1, VE(hr.GetMean(),hr.GetStdDev()**2 ))
        print("Z="+str(inZ)+"\tR="+str(inR)+"\tdr="+str(hr.GetMean()))

hR.GetZaxis().SetRangeUser(0,1.)
hR.Draw("colz")

file = ROOT.TFile("radial_shift.root", "RECREATE")
hR.Write()

