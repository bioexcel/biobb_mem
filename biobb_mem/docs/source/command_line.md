# BioBB MEM Command Line Help
Generic usage:
```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


## Assign_leaflets
Wrapper of the Lipyphilic AssignLeaflets module for assigning lipids to leaflets in a bilayer.
### Get help
Command:
```python
assign_leaflets -h
```
    usage: assign_leaflets [-h] [--config CONFIG] --input_top_path INPUT_TOP_PATH --input_traj_path INPUT_TRAJ_PATH --output_leaflets_path OUTPUT_LEAFLETS_PATH
    
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
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/data/A01JD/A01JD.pdb). Accepted formats: CRD, GRO, MDCRD, MOL2, PDB, PDBQT, PRMTOP, PSF, TOP, TPR, XML, XYZ
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/data/A01JD/A01JD.xtc). Accepted formats: ARC, CRD, DCD, ENT, GRO, INPCRD, MDCRD, MOL2, NC, PDB, PDBQT, RESTRT, TNG, TRR, XTC, XYZ
* **output_leaflets_path** (*string*): Path to the output leaflet assignments. File type: output. [Sample file](https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/reference/lipyphilicBB/leaflets.csv). Accepted formats: CSV
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
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
### YAML
### JSON

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
* **input_top_path** (*string*): Path to the input structure or topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/data/ambertools/topology.top). Accepted formats: TOP, PDB, PRMTOP, PARMTOP, ZIP
* **input_traj_path** (*string*): Path to the input trajectory to be processed. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/data/ambertools/trajectory.xtc). Accepted formats: MDCRD, CRD, CDF, NETCDF, NC, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
* **output_cpptraj_path** (*string*): Path to the output processed density analysis. File type: output. [Sample file](https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/reference/ambertools/reference/density_default.dat). Accepted formats: DAT, AGR, XMGR, GNU
* **output_traj_path** (*string*): Path to the output processed trajectory. File type: output. [Sample file](https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/reference/ambertools/trajectory_out.dcd). Accepted formats: MDCRD, CRD, CDF, NETCDF, NC, RESTART, NCRESTART, RESTARTNC, DCD, CHARMM, COR, PDB, MOL2, TRR, GRO, BINPOS, XTC, CIF, ARC, SQM, SDF, CONFLIB
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
### JSON

## Chap_run
Wrapper of the Channel Annotation Package (CHAP) for analyzing pore geometry, hydrophobicity, and hydration state in protein channels and other macromolecular structures.
### Get help
Command:
```python
chap_run -h
```
    /bin/sh: line 1: chap_run: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_top_path** (*string*): Path to the input  topology file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/data/A01JD/A01JD.pdb). Accepted formats: TPR, GRO, G96, PDB, BRK, ENT
* **input_traj_path** (*string*): Path to the GROMACS trajectory file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/data/A01JD/A01JD.xtc). Accepted formats: XTC, TRR, CPT, GRO, G96, PDB, TNG
* **input_index_path** (*string*): Path to the GROMACS index file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/data/A01JD/A01JD.ndx). Accepted formats: NDX
* **output_obj_path** (*string*): Path to the output Wavefront Object file containing CHAP results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/reference/chap/chap_output.obj). Accepted formats: OBJ
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **b** (*number*): (None) First frame (in picoseconds) to read from trajectory..
* **e** (*number*): (None) Last frame (in picoseconds) to read from trajectory..
* **df** (*number*): (None) Only use frame if t MOD dt == first time (in picoseconds)..
* **tu** (*string*): (ps) Unit for time values..
* **sel_pathway** (*string*): (None) Reference group that defines the permeation pathway (usually 'Protein')..
* **sel_solvent** (*string*): (None) Group of small particles to calculate density of (usually 'Water')..
* **out_filename** (*string*): (chap_output) Base file name for output files without file extension..
* **out_num_points** (*integer*): (1000) Number of spatial sample points that are written to the JSON output file..
* **out_extrap_dist** (*number*): (0.0) Extrapolation distance beyond the pathway endpoints for both JSON and OBJ output..
* **out_grid_dist** (*number*): (0.15) Controls the sampling distance of vertices on the pathway surface which are subsequently interpolated to yield a smooth surface. Very small values may yield visual artifacts..
* **out_vis_tweak** (*number*): (0.1) Visual tweaking factor that controls the smoothness of the pathway surface in the OBJ output. Varies between -1 and 1 (exclusively), where larger values result in a smoother surface. Negative values may result in visualisation artifacts..
* **out_detailed** (*boolean*): (False) If true, CHAP will write detailed per-frame information to a newline delimited JSON file including original probe positions and spline parameters. This is mostly useful for debugging..
* **pf_method** (*string*): (inplane_optim) Path finding method. The default inplane_optim implements the algorithm used in the HOLE programme, where the position of a probe sphere is optimised in subsequent parallel planes so as to maximise its radius. The alternative cylindrical simply uses a cylindrical volume as permeation pathway..
* **pf_vdwr_database** (*string*): (hole_simple) Database of van-der-Waals radii to be used in pore finding..
* **pf_vdwr_fallback** (*number*): (None) Fallback van-der-Waals radius for atoms that are not listed in van-der-Waals radius database. Unless this is set to a positive value, an error will be thrown if a pathway-forming atom has no associated van-der-Waals radius in the database..
* **pf_vdwr_json** (*string*): (None) JSON file with user defined van-der-Waals radii. Will be ignored unless -pf-vdwr-database is set to 'user'..
* **pf_align_method** (*string*): (ipp) Method for aligning pathway coordinates across time steps..
* **pf_probe_step** (*number*): (0.1) Step length for probe movement..
* **pf_max_free_dist** (*number*): (1.0) Maximum radius of pore..
* **pf_max_probe_steps** (*integer*): (10000) Maximum number of steps the probe is moved in either direction..
* **pf_sel_ipp** (*string*): (None) Selection of atoms whose COM will be used as initial probe position. If not set, the selection specified with 'sel-pathway' will be used..
* **pf_init_probe_pos** (*array*): (None) Initial position of probe in probe-based pore finding algorithms. If set explicitly, it will overwrite the COM-based initial position set with the ippSelflag..
* **pf_chan_dir_vec** (*array*): ([0.0, 0.0, 1.0]) Channel direction vector. Will be normalised to unit vector internally..
* **pf_cutoff** (*number*): (None) Cutoff for distance searches in path finding algorithm. A value of zero or less means no cutoff is applied. If unset, an appropriate cutoff is determined automatically..
* **sa_seed** (*integer*): (None) Seed used in pseudo random number generation for simulated annealing. If not set explicitly, a random seed is used..
* **sa_max_iter** (*integer*): (0) Number of cooling iterations in one simulated annealing run..
* **sa_init_temp** (*number*): (0.1) Simulated annealing initial temperature..
* **sa_cooling_fac** (*number*): (0.98) Simulated annealing cooling factor..
* **sa_step** (*number*): (0.001) Step length factor used in candidate generation..
* **nm_max_iter** (*integer*): (100) Number of Nelder-Mead simplex iterations in path finding algorithm..
* **nm_init_shift** (*number*): (0.1) Distance of vertices in initial Nelder-Mead simplex..
* **pm_pl_margin** (*number*): (0.75) Margin for determining pathway lining residues. A residue is considered to be pathway lining if it is no further than the local path radius plus this margin from the pathway's centre line..
* **pm_pf_sel** (*string*): (name CA) Distance of vertices in initial Nelder-Mead simplex..
* **de_method** (*string*): (kernel) Method used for estimating the probability density of the solvent particles along the permeation pathway..
* **de_res** (*number*): (0.01) Spatial resolution of the density estimator. In case of a histogram, this is the bin width, in case of a kernel density estimator, this is the spacing of the evaluation points..
* **de_bandwidth** (*number*): (-1.0) Bandwidth for the kernel density estimator. Ignored for other methods. If negative or zero, bandwidth will be determined automatically to minimise the asymptotic mean integrated squared error (AMISE)..
* **de_bw_scale** (*number*): (1.0) Scaling factor for the band width. Useful to set a bandwidth relative to the AMISE-optimal value..
* **de_eval_cutoff** (*number*): (5.0) Evaluation range cutoff for kernel density estimator in multiples of bandwidth. Ignored for other methods. Ensures that the density falls off smoothly to zero outside the data range..
* **hydrophob_database** (*string*): (wimley_white_1996) Database of hydrophobicity scale for pore forming residues..
* **hydrophob_fallback** (*number*): (None) Fallback hydrophobicity for residues in the pathway defining group. If unset, residues missing in the database will cause an error.".
* **hydrophob_json** (*string*): (None) JSON file with user defined hydrophobicity scale. Will be ignored unless -hydrophobicity-database is set to 'user'..
* **hydrophob_bandwidth** (*number*): (0.35) Bandwidth for hydrophobicity kernel..
* **binary_path** (*string*): (chap) Path to the CHAP executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
### YAML
### JSON
