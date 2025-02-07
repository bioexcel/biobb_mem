# BioBB MEM Command Line Help
Generic usage:
```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


## Cpptraj_density
Wrapper of the Ambertools Cpptraj module for calculating density profile along an axis of a given cpptraj compatible trajectory.
### Get help
Command:
```python
cpptraj_density -h
```
    usage: cpptraj_density [-h] [--config CONFIG] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_cpptraj_path OUTPUT_CPPTRAJ_PATH [--output_traj_path OUTPUT_TRAJ_PATH]
    
    Calculates the density along an axis of a given cpptraj compatible trajectory.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --output_traj_path OUTPUT_TRAJ_PATH
                            Path to the output processed trajectory.
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: top, pdb, prmtop, parmtop, zip.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: crd, cdf, netcdf, restart, ncrestart, restartnc, dcd, charmm, cor, pdb, mol2, trr, gro, binpos, xtc, cif, arc, sqm, sdf, conflib.
      --output_cpptraj_path OUTPUT_CPPTRAJ_PATH
                            Path to the output processed analysis.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/ambertools/topology.top). Accepted formats: TOP, PDB, PRMTOP, PARMTOP, ZIP
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/ambertools/trajectory.xtc). Accepted formats: MDCRD, CRD, CDF, NETCDF, NC, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
* **output_cpptraj_path** (*string*): Path to the output processed density analysis. File type: output. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/reference/ambertools/reference/density_default.dat). Accepted formats: DAT, AGR, XMGR, GNU
* **output_traj_path** (*string*): Path to the output processed trajectory. File type: output. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/reference/ambertools/trajectory_out.dcd). Accepted formats: MDCRD, CRD, CDF, NETCDF, NC, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (1) Starting frame for slicing.
* **end** (*integer*): (-1) Ending frame for slicing.
* **steps** (*integer*): (1) Step for slicing.
* **density_type** (*string*): (number) Number, mass, partial charge (q) or electron (Ne - q) density. Electron density will be converted to e-/Å3 by dividing the average area spanned by the other two dimensions..
* **mask** (*string*): (*) Arbitrary number of masks for atom selection; a dataset is created and the output will contain entries for each mask.. Default: all atoms..
* **delta** (*number*): (0.25) Resolution, i.e. determines number of slices (i.e. histogram bins)..
* **axis** (*string*): (z) Coordinate (axis) for density calculation. Vales: x, y, z..
* **bintype** (*string*): (bincenter) Determine whether histogram bin coordinates will be based on bin center (default) or bin edges. .
* **restrict** (*string*): (None) If specified, only calculate the density within a cylinder or square shape from the specified axis as defined by a distance cutoff. .
* **cutoff** (*number*): (None) The distance cutoff for 'restrict'. Required if 'restrict' is specified..
* **binary_path** (*string*): (cpptraj) Path to the cpptraj executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mem/blob/master/biobb_mem/test/data/config/config_cpptraj_density.yml)
```python
properties:
  disable_logs: true

```
#### Command line
```python
cpptraj_density --config config_cpptraj_density.yml --input_top_path topology.top --input_traj_path trajectory.xtc --output_cpptraj_path density_default.dat --output_traj_path trajectory_out.dcd
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mem/blob/master/biobb_mem/test/data/config/config_cpptraj_density.json)
```python
{
  "properties": {
    "disable_logs": true
  }
}
```
#### Command line
```python
cpptraj_density --config config_cpptraj_density.json --input_top_path topology.top --input_traj_path trajectory.xtc --output_cpptraj_path density_default.dat --output_traj_path trajectory_out.dcd
```

## Lpp_assign_leaflets
Wrapper of the LiPyphilic AssignLeaflets module for assigning lipids to leaflets in a bilayer.
### Get help
Command:
```python
lpp_assign_leaflets -h
```
    usage: lpp_assign_leaflets [-h] [--config CONFIG] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_leaflets_path OUTPUT_LEAFLETS_PATH
    
    Assign lipids to leaflets in a bilayer.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: crd, gro, mdcrd, mol2, pdb, pdbqt, prmtop, psf, top, tpr, xml, xyz.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: arc, crd, dcd, ent, gro, inpcrd, mdcrd, mol2, nc, pdb, pdbqt, restrt, tng, trr, xtc, xyz.
      --output_leaflets_path OUTPUT_LEAFLETS_PATH
                            Path to the output processed analysis.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.pdb). Accepted formats: CRD, GRO, MDCRD, MOL2, PDB, PDBQT, PRMTOP, PSF, TOP, TPR, XML, XYZ
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.xtc). Accepted formats: ARC, CRD, DCD, ENT, GRO, INPCRD, MDCRD, MOL2, NC, PDB, PDBQT, RESTRT, TNG, TRR, XTC, XYZ
* **output_leaflets_path** (*string*): Path to the output leaflet assignments. File type: output. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/reference/lipyphilic_biobb/leaflets_data.csv). Accepted formats: CSV, NPY
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (None) Starting frame for slicing..
* **stop** (*integer*): (None) Ending frame for slicing..
* **steps** (*integer*): (None) Step for slicing..
* **lipid_sel** (*string*): (all) Selection string for the lipids in a membrane. The selection should cover **all** residues in the membrane, including cholesterol..
* **midplane_sel** (*string*): (None) Selection string for residues that may be midplane. Any residues not in this selection will be assigned to a leaflet regardless of its proximity to the midplane. The default is `None`, in which case all lipids will be assigned to either the upper or lower leaflet..
* **midplane_cutoff** (*number*): (0.0) Minimum distance in *z* an atom must be from the midplane to be assigned to a leaflet rather than the midplane. The default is `0`, in which case all lipids will be assigned to either the upper or lower leaflet. Must be non-negative..
* **n_bins** (*integer*): (1) Number of bins in *x* and *y* to use to create a grid of membrane patches. Local membrane midpoints are computed for each patch, and lipids assigned a leaflet based on the distance to their local membrane midpoint. The default is `1`, which is equivalent to computing a single global midpoint..
* **ignore_no_box** (*boolean*): (False) Ignore the absence of box information in the trajectory. If the trajectory does not contain box information, the box will be set to the minimum and maximum positions of the atoms in the trajectory..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mem/blob/master/biobb_mem/test/data/config/config_lpp_assign_leaflets.yml)
```python
properties:
  disable_logs: true
  ignore_no_box: true
  lipid_sel: (resname DPPC and name P8)

```
#### Command line
```python
lpp_assign_leaflets --config config_lpp_assign_leaflets.yml --input_top_path A01JD.pdb --input_traj_path A01JD.xtc --output_leaflets_path leaflets_data.csv
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mem/blob/master/biobb_mem/test/data/config/config_lpp_assign_leaflets.json)
```python
{
  "properties": {
    "disable_logs": true,
    "ignore_no_box": true,
    "lipid_sel": "(resname DPPC and name P8)"
  }
}
```
#### Command line
```python
lpp_assign_leaflets --config config_lpp_assign_leaflets.json --input_top_path A01JD.pdb --input_traj_path A01JD.xtc --output_leaflets_path leaflets_data.csv
```

## Lpp_zpositions
Wrapper of the LiPyphilic ZPositions module for calculating the z distance of lipids to the bilayer center.
### Get help
Command:
```python
lpp_zpositions -h
```
    usage: lpp_zpositions [-h] [--config CONFIG] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_positions_path OUTPUT_POSITIONS_PATH
    
    Calculate the z distance in of lipids to the bilayer center.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: crd, gro, mdcrd, mol2, pdb, pdbqt, prmtop, psf, top, tpr, xml, xyz.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: arc, crd, dcd, ent, gro, inpcrd, mdcrd, mol2, nc, pdb, pdbqt, restrt, tng, trr, xtc, xyz.
      --output_positions_path OUTPUT_POSITIONS_PATH
                             Path to the output z positions.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.pdb). Accepted formats: CRD, GRO, MDCRD, MOL2, PDB, PDBQT, PRMTOP, PSF, TOP, TPR, XML, XYZ
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.xtc). Accepted formats: ARC, CRD, DCD, ENT, GRO, INPCRD, MDCRD, MOL2, NC, PDB, PDBQT, RESTRT, TNG, TRR, XTC, XYZ
* **output_positions_path** (*string*): Path to the output z positions. File type: output. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/reference/lipyphilic_biobb/zpositions.csv). Accepted formats: CSV
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (None) Starting frame for slicing..
* **stop** (*integer*): (None) Ending frame for slicing..
* **steps** (*integer*): (None) Step for slicing..
* **lipid_sel** (*string*): (all) Selection string for the lipids in a membrane. The selection should cover **all** residues in the membrane, including cholesterol..
* **height_sel** (*string*): (all) Atom selection for the molecules for which the z position will be calculated..
* **n_bins** (*integer*): (1) Number of bins in *x* and *y* to use to create a grid of membrane patches. Local membrane midpoints are computed for each patch, and lipids assigned a leaflet based on the distance to their local membrane midpoint. The default is `1`, which is equivalent to computing a single global midpoint..
* **ignore_no_box** (*boolean*): (False) Ignore the absence of box information in the trajectory. If the trajectory does not contain box information, the box will be set to the minimum and maximum positions of the atoms in the trajectory..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mem/blob/master/biobb_mem/test/data/config/config_lpp_zpositions.yml)
```python
properties:
  disable_logs: true
  height_sel: (resname DPPC and name P8)
  ignore_no_box: true
  lipid_sel: (resname DPPC and name P8)

```
#### Command line
```python
lpp_zpositions --config config_lpp_zpositions.yml --input_top_path A01JD.pdb --input_traj_path A01JD.xtc --output_positions_path zpositions.csv
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mem/blob/master/biobb_mem/test/data/config/config_lpp_zpositions.json)
```python
{
  "properties": {
    "disable_logs": true,
    "ignore_no_box": true,
    "lipid_sel": "(resname DPPC and name P8)",
    "height_sel": "(resname DPPC and name P8)"
  }
}
```
#### Command line
```python
lpp_zpositions --config config_lpp_zpositions.json --input_top_path A01JD.pdb --input_traj_path A01JD.xtc --output_positions_path zpositions.csv
```

## Mda_hole
Wrapper of the MDAnalysis HOLE module for analyzing ion channel pores or transporter pathways.
### Get help
Command:
```python
mda_hole -h
```
    usage: mda_hole [-h] [--config CONFIG] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_hole_path OUTPUT_HOLE_PATH --output_csv_path OUTPUT_CSV_PATH
    
    Analyze ion channel pores or transporter pathways.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: crd, gro, mdcrd, mol2, pdb, pdbqt, prmtop, psf, top, tpr, xml, xyz.
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: arc, crd, dcd, ent, gro, inpcrd, mdcrd, mol2, nc, pdb, pdbqt, restrt, tng, trr, xtc, xyz.
      --output_hole_path OUTPUT_HOLE_PATH
                            Path to the output HOLE analysis results. Accepted formats: vmd.
      --output_csv_path OUTPUT_CSV_PATH
                            Path to the output CSV file containing the radius and coordinates of the pore. Accepted formats: csv.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.pdb). Accepted formats: CRD, GRO, MDCRD, MOL2, PDB, PDBQT, PRMTOP, PSF, TOP, TPR, XML, XYZ
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.xtc). Accepted formats: ARC, CRD, DCD, ENT, GRO, INPCRD, MDCRD, MOL2, NC, PDB, PDBQT, RESTRT, TNG, TRR, XTC, XYZ
* **output_hole_path** (*string*): Path to the output HOLE analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/reference/mdanalysis_biobb/hole.vmd). Accepted formats: VMD
* **output_csv_path** (*string*): Path to the output CSV file containing the radius and coordinates of the pore. File type: output. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/reference/mdanalysis_biobb/hole_profile.csv). Accepted formats: CSV
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (None) Starting frame for slicing..
* **stop** (*integer*): (None) Ending frame for slicing..
* **steps** (*integer*): (None) Step for slicing..
* **executable** (*string*): (hole) Path to the HOLE executable..
* **select** (*string*): (protein) The selection string to create an atom selection that the HOLE analysis is applied to..
* **cpoint** (*array*): (None) Coordinates of a point inside the pore (Å). If None, tries to guess based on the geometry..
* **cvect** (*array*): (None) Search direction vector. If None, tries to guess based on the geometry..
* **sample** (*number*): (0.2) Distance of sample points in Å. This value determines how many points in the pore profile are calculated..
* **end_radius** (*number*): (22.0) Radius in Å, which is considered to be the end of the pore..
* **dot_density** (*integer*): (15) Density of facets for generating a 3D pore representation..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mem/blob/master/biobb_mem/test/data/config/config_mda_hole.yml)
```python
properties:
  disable_logs: true
  select: protein
  steps: 5

```
#### Command line
```python
mda_hole --config config_mda_hole.yml --input_top_path A01JD.pdb --input_traj_path A01JD.xtc --output_hole_path hole.vmd --output_csv_path hole_profile.csv
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mem/blob/master/biobb_mem/test/data/config/config_mda_hole.json)
```python
{
  "properties": {
    "disable_logs": true,
    "select": "protein",
    "steps": 5
  }
}
```
#### Command line
```python
mda_hole --config config_mda_hole.json --input_top_path A01JD.pdb --input_traj_path A01JD.xtc --output_hole_path hole.vmd --output_csv_path hole_profile.csv
```

## Lpp_flip_flop
Wrapper of the LiPyphilic FlipFlop module for finding flip-flop events in a lipid bilayer.
### Get help
Command:
```python
lpp_flip_flop -h
```
    /bin/sh: 1: lpp_flip_flop: not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.pdb). Accepted formats: CRD, GRO, MDCRD, MOL2, PDB, PDBQT, PRMTOP, PSF, TOP, TPR, XML, XYZ
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.xtc). Accepted formats: ARC, CRD, DCD, ENT, GRO, INPCRD, MDCRD, MOL2, NC, PDB, PDBQT, RESTRT, TNG, TRR, XTC, XYZ
* **input_leaflets_path** (*string*): Path to the input leaflet assignments. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/reference/lipyphilic_biobb/leaflets_data.csv). Accepted formats: CSV, NPY
* **output_flip_flop_path** (*string*): Path to the output flip-flop data. File type: output. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/reference/lipyphilic_biobb/flip_flop.csv). Accepted formats: CSV
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **start** (*integer*): (None) Starting frame for slicing..
* **stop** (*integer*): (None) Ending frame for slicing..
* **steps** (*integer*): (None) Step for slicing..
* **lipid_sel** (*string*): (all) Selection string for the lipids in a membrane. The selection should cover **all** residues in the membrane, including cholesterol..
* **frame_cutoff** (*number*): (1.0) To be counted as a successful flip-flop, a molecule must reside in its new leaflet for at least ‘frame_cutoff’ consecutive frames. The default is 1, in which case the molecule only needs to move to the opposing leaflet for a single frame for the flip-flop to be successful..
* **ignore_no_box** (*boolean*): (False) Ignore the absence of box information in the trajectory. If the trajectory does not contain box information, the box will be set to the minimum and maximum positions of the atoms in the trajectory..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mem/blob/master/biobb_mem/test/data/config/config_lpp_flip_flop.yml)
```python
properties:
  disable_logs: true
  ignore_no_box: true
  lipid_sel: (resname DPPC and name P8)

```
#### Command line
```python
lpp_flip_flop --config config_lpp_flip_flop.yml --input_top_path A01JD.pdb --input_traj_path A01JD.xtc --input_leaflets_path leaflets_data.csv --output_flip_flop_path flip_flop.csv
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mem/blob/master/biobb_mem/test/data/config/config_lpp_flip_flop.json)
```python
{
  "properties": {
    "disable_logs": true,
    "ignore_no_box": true,
    "lipid_sel": "(resname DPPC and name P8)"
  }
}
```
#### Command line
```python
lpp_flip_flop --config config_lpp_flip_flop.json --input_top_path A01JD.pdb --input_traj_path A01JD.xtc --input_leaflets_path leaflets_data.csv --output_flip_flop_path flip_flop.csv
```

## Fatslim_membranes
Wrapper of the FATSLiM membranes module for leaflet and membrane identification.
### Get help
Command:
```python
fatslim_membranes -h
```
    usage: fatslim_membranes [-h] [--config CONFIG] --input_top_path INPUT_TOP_PATH --output_ndx_path OUTPUT_NDX_PATH [--input_traj_path INPUT_TRAJ_PATH] [--input_ndx_path INPUT_NDX_PATH]
    
    Calculates the density along an axis of a given cpptraj compatible trajectory.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --input_traj_path INPUT_TRAJ_PATH
                            Path to the input trajectory to be processed. Accepted formats: gro, pdb, tng, trr, xtc.
      --input_ndx_path INPUT_NDX_PATH
                            Path to the input lipid headgroups index NDX file. Accepted formats: ndx.
    
    required arguments:
      --input_top_path INPUT_TOP_PATH
                            Path to the input structure or topology file. Accepted formats: ent, gro, pdb, tpr.
      --output_ndx_path OUTPUT_NDX_PATH
                            Path to the GROMACS index file. Accepted formats: ndx
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.pdb). Accepted formats: TPR, GRO, G96, PDB, BRK, ENT
* **input_traj_path** (*string*): Path to the GROMACS trajectory file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.xtc). Accepted formats: XTC, TRR, CPT, GRO, G96, PDB, TNG
* **input_ndx_path** (*string*): Path to the input lipid headgroups index NDX file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.ndx). Accepted formats: NDX
* **output_ndx_path** (*string*): Path to the output index NDX file. File type: output. [Sample file](https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/reference/fatslim/leaflets.ndx). Accepted formats: NDX
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **selection** (*string*): (not protein and element P) Alternative ot the NDX file for choosing the Headgroups used in the identification using MDAnalysis selection language..
* **cutoff** (*number*): (2.0) Cutoff distance (in nm) to be used when leaflet identification is performed..
* **begin_frame** (*integer*): (-1) First frame index to be used for analysis..
* **end_frame** (*integer*): (-1) Last frame index to be used for analysis..
* **ignore_no_box** (*boolean*): (False) Ignore the absence of box information in the topology. If the topology does not contain box information, the box will be set to the minimum and maximum positions of the atoms..
* **return_hydrogen** (*boolean*): (False) Include hydrogen atoms in the output index file..
* **binary_path** (*string*): (fatslim) Path to the fatslim executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mem/blob/master/biobb_mem/test/data/config/config_fatslim_membranes.yml)
```python
properties:
  cutoff: 2.2
  disable_logs: true
  ignore_no_box: true
  selection: (resname DPPC and name P8)

```
#### Command line
```python
fatslim_membranes --config config_fatslim_membranes.yml --input_top_path A01JD.pdb --input_traj_path A01JD.xtc --input_ndx_path A01JD.ndx --output_ndx_path leaflets.ndx
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mem/blob/master/biobb_mem/test/data/config/config_fatslim_membranes.json)
```python
{
  "properties": {
    "disable_logs": true,
    "ignore_no_box": true,
    "selection": "(resname DPPC and name P8)",
    "cutoff": 2.2
  }
}
```
#### Command line
```python
fatslim_membranes --config config_fatslim_membranes.json --input_top_path A01JD.pdb --input_traj_path A01JD.xtc --input_ndx_path A01JD.ndx --output_ndx_path leaflets.ndx
```
