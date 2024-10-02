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
## Method

Electron is drifted in the electric field. Its track is a series of the steps, defined by a `step` parameter. A typical step size (of 0.1 mm) is order of magnitude less than a spatial grid size for the electric field (5 mm). A direction for the step is choosen according to a unit vector parallel to an electric field direction. Electric field components in a beggining of a step are infered by an interpolation procedure (tri-linear interpolation).

## Available scripts

 *  `module.py` - defines a trace function which tracks one electron according to the electric field and finds its X- and Y-positions at the grid-plane (Z=0) and as well as a Gaussian diffuser, common to the rest of the programms.
 * `create_histo.py` - create `ROOT.TH3F` for field components and store it in a root-file. **The other programs depend on this rootfile, so it's necesary to execute this program firts for everything to work properly.**
 * `test_histo.py` - test that histograms can be readed from root-file;
 * `trace_electron.py` - generates random points on a ring with r and z fixed, applies the trace function for every point and studies the correlation between the phi_in and phi_out coordinates.
 * `radial_shift.py` - create 2D-map with a radial shift depending on initial Z- and R-position (phi-averaged).
 

## Results

 * No radial shift if Ex and Ey are set to zero (red histo on **dr_z290_R211.png**);
 * Some radial shift for the full field map (see **dr_z290_R211.png**, Rin=211mm, Zin=290mm, phi-averaged);
 * The direction of this is to the center of TPC ( phi_shift = -phi_in, see **shift_dir.png**);
 * There is strong Rin and Zin pependens (see 2D-png-files).
 


