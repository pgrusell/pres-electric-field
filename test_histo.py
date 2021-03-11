h2_Ex = ROOT.TH2F("h2_Ex","x-componet of electric field;z, mm,;r, mm",
                    61, -2.5, 302.5 ,201,-0.5, 200.5)
h2_Ey = ROOT.TH2F("h2_Ey","y-componet of electric field;x, mm;y, mm;z, mm",
                    61, -2.5, 302.5 ,201,-0.5, 200.5)
h2_Ez = ROOT.TH2F("h2_Ez","z-componet of electric field;x, mm;y, mm;z, mm",
                    61, -2.5, 302.5 ,201,-0.5, 200.5)


rfile = ROOT.TFile('histo.root',"READ")
h3_Ex = rfile["h3_Ex"]
h3_Ey = rfile["h3_Ey"]
h3_Ez = rfile["h3_Ez"]

from math import pi, sin, cos, tan
from statistics import mean, stdev


for k in range(1,62):
    z = 5.*(k-1)
    for i in range(1,202):
        r = float(i-1)
        vx = [] ; vy = [] ; vz = []
        for j in range(60):
            phi = 2.*pi*j/60.
            x = r*cos(phi)
            y = r*sin(phi)
            vx.append( h3_Ex(x,y,z).value() )
            vy.append( h3_Ey(x,y,z).value() )
            vz.append( h3_Ez(x,y,z).value() )
        h2_Ex[ (k,i) ] = VE( mean(vx), 0.0001**2)
        h2_Ey[ (k,i) ] = VE( mean(vy), 0.0001**2)
        h2_Ez[ (k,i) ] = VE( mean(vz),10**2)

#rfile.Close()


