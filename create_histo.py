
h3_Ex = ROOT.TH3F("h3_Ex","x-componet of electric field;x, mm;y, mm;z, mm",
                    101, -252.5, 252.5, 101,-252.5, 252.5, 61, -2.5, 302.5 )
h3_Ey = ROOT.TH3F("h3_Ey","y-componet of electric field;x, mm;y, mm;z, mm",
                    101, -252.5, 252.5, 101,-252.5, 252.5, 61, -2.5, 302.5 )
h3_Ez = ROOT.TH3F("h3_Ez","z-componet of electric field;x, mm;y, mm;z, mm",
                    101, -252.5, 252.5, 101,-252.5, 252.5, 61, -2.5, 302.5 )

print("LOADING FIELD MAP INTO TH3F")
with open("pres-electric-field.txt","r") as tfile:
    cnt = 0
    for line in tfile:
        if line[0]!="%":
            elements = line[:-1].split(" ")
            values = []
            for w in elements:
                if w:
                    values.append( float(w)  )
            i = 1 + int( ( values[0] + 250.)/5. )
            j = 1 + int( ( values[1] + 250.)/5. )
            k = 1 + int( ( values[2]       )/5. )
            h3_Ex[ (i,j,k) ] = VE( values[3],  0.0001**2 )
            h3_Ey[ (i,j,k) ] = VE( values[4],  0.0001**2 )
            h3_Ez[ (i,j,k) ] = VE( values[5], 10.0000**2 )
            if cnt<10:
                print(line[:-1])
                print(values)
                print(i)
                print(j)
                print(k)
                cnt += 1
print("LOADING IS DONE")


with ROOT.TFile('histo.root',"RECREATE") as rfile :
    rfile["h3_Ex"] = h3_Ex
    rfile["h3_Ey"] = h3_Ey
    rfile["h3_Ez"] = h3_Ez


