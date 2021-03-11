# Electron drift in PRES TPC

Electric field calculations are done by Kuzma Ivshin using COMSOL package.
One can download 50Mb file by
```bash
wget http://adzyuba.web.cern.ch/adzyuba/d/pres-electric-field.txt
```

The software is working in the conda evoirment. 
See https://github.com/aleksha/pres-mc for details.
To active envoirment one have to install it ant then type:
```bash
conda activate pres-mc
```

## Available scripts

 * `create_histo.py` - create `ROOT.TH3F` for field components and store it in a root-file;
 * `test_histo.py` - test that histograms can be readed from root-file;
 * `trace_electron.py` - trace one electron according electric filed and find its X- and Y-positions at the grid-plane (Z=0)
 * 'radial_shift.py' - create 2D-map with a radial shift depending on initial Z- and R-position (phi-averaged).

## Results

 * No radial shift if Ex and Ey are set to zero (red histo on **dr_z290_R211.png**);
 * Some radial shift for the full field map (see **dr_z290_R211.png**, Rin=211mm, Zin=290mm, phi-averaged);
 * There is strong Rin and Zin pependens (see 2D-png-files).
 


