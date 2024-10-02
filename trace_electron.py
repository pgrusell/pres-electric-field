import ROOT
from module import *
from math import pi, sin, cos, tan, sqrt
from statistics import mean, stdev
from random import random
from   ostap.utils.progress_bar import progress_bar

inR = 210.
inZ = 280.

rfile = ROOT.TFile('histo.root',"READ")

h3_Ex = rfile.Get("h3_Ex")
h3_Ey = rfile.Get("h3_Ey")
h3_Ez = rfile.Get("h3_Ez")

hl = ROOT.TH1F("hl","length - z", 200, -0.01, 2.9)
hn = ROOT.TH1F("hn","length - z", 200, -0.01, 2.9)
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
    hl.Fill( 1000.*(track_length-inZ) )
    hr.Fill( dr )
    pos, track_length = trace(inX, inY, inZ , h3_Ex, h3_Ey, h3_Ez, field=(False,False,True))
    outX, outY = pos.x(), pos.y()
    dr = sqrt((outX-inX)**2+(outY-inY)**2)
    hn.Fill( 1000.*(track_length-inZ) )
    ht.Fill( dr )

hr.Draw()
ht.Draw("same")

h_dir.GetXaxis().SetTitleSize(0.04)
h_dir.GetYaxis().SetTitleSize(0.04)
h_dir.Draw("col")

file = ROOT.TFile("electron_trace.root", "RECREATE")
h_dir.Write()
